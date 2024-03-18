import os
import requests
import spotipy
import colorsys
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import io
from sklearn.cluster import KMeans
import numpy as np
import time

# Global constants
REDIRECT_URI = 'http://localhost:8000'
CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".spotify_cache")
SELECTOR = 'all'
TRANSITION_DURATION = 5

#Spotify setup
def setup_spotify():
    scope = "user-read-currently-playing"
    spotify_client_id = 'YOUR CLIENT ID'
    spotify_client_secret = 'YOUR CLIENT SECRET'
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri=REDIRECT_URI, cache_path=CACHE_PATH))

#LIFX setup
def get_lifx_headers():
    lifx_token = 'c38bf06dabe869aa0b51a0b00298b4d6d1d50e13afe5238121be19b58110de9a'
    return {"Authorization": f"Bearer {lifx_token}"}

#Convert image to RGB and extract dominant colors
def extract_colors_from_image(img, n_clusters=5):
    img = img.convert('RGB')
    pixels = np.array(img).reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_clusters, n_init=10).fit(pixels)
    return kmeans.cluster_centers_

#Convert RGB to HSB for LIFX API
def convert_to_hsb(color):
    hsb_color = colorsys.rgb_to_hsv(color[0]/255, color[1]/255, color[2]/255)
    return "hsb:{:.2f},{:.2f},{:.2f}".format(hsb_color[0]*360, hsb_color[1], 1.0)

def main():
    #Initialize spotify client and get LIFX headers
    sp = setup_spotify()
    headers = get_lifx_headers()

    last_track_id = None
    last_lifx_colors = None

    while True:
        #Get current track
        current_track = sp.current_user_playing_track()
        current_track_id = current_track['item']['id']

        track_name = current_track['item']['name']
        artist_names = [artist['name'] for artist in current_track['item']['artists']]

        if current_track_id != last_track_id:
            #If a new track is playing, get the album art URL
            album_art_url = current_track['item']['album']['images'][0]['url']
            response = requests.get(album_art_url)
            print(f"Currently playing: {track_name} by {' & '.join(artist_names)}")
            img = Image.open(io.BytesIO(response.content))
            colors = extract_colors_from_image(img)

            #Convert extracted colors to HSB
            lifx_colors = [convert_to_hsb(color) for color in colors]

            if lifx_colors != last_lifx_colors:
                while True:
                    for color in lifx_colors:
                        # Check if song has changed during color cycle
                        current_check = sp.current_user_playing_track()
                        if current_check['item']['id'] != current_track_id:
                            break

                        payload = {
                            'power': 'on',
                            'color': color,
                            'brightness': 1.0,
                            'duration': TRANSITION_DURATION
                        }

                        # Send request to LIFX API
                        response = requests.put(f'https://api.lifx.com/v1/lights/{SELECTOR}/state', headers=headers, data=payload)
                        time.sleep(TRANSITION_DURATION)
                    else:
                        # If the inner loop wasn't broken because of a song change, continue cycling.
                        continue

                    # If inner loop was broken because of song change, break the while loop too.
                    break

        last_track_id = current_track_id
        last_lifx_colors = lifx_colors[:]

    time.sleep(5)

if __name__ == "__main__":
    main()

