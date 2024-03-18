Spotify Album Art Color Sync with LIFX Lights

This Python script dynamically changes the colors of your LIFX lights based on the dominant colors of the currently playing Spotify track's album art. It uses the Spotify API to fetch the current track information and the album art image. The dominant colors are extracted using KMeans clustering provided by scikit-learn. These colors are then converted to the HSB color model, which is compatible with LIFX lights, to set the light colors accordingly.

Features
Fetches currently playing track information using the Spotify API.
Downloads the album art of the current track.
Extracts five dominant colors from the album art using KMeans clustering.
Converts RGB colors to HSB (Hue, Saturation, Brightness) for LIFX compatibility.
Cycles through the extracted colors on your LIFX lights.
Setup
Spotify API: You need to have a Spotify Developer account to create an app and get your Client ID and Client Secret. Also, set the Redirect URI to http://localhost:8000.
LIFX Token: Generate a LIFX token from the LIFX Cloud HTTP API to control your lights.
Python Libraries: This script requires spotipy, requests, PIL, numpy, scikit-learn, and a few other libraries. Make sure to install these dependencies.
Configuration
Replace YOUR CLIENT ID and YOUR CLIENT SECRET with your Spotify App credentials.
Update lifx_token with your LIFX API token.
Optionally, customize the selector variable to target specific lights.
Running the Script
Simply run the script while playing music on Spotify. Your LIFX lights will automatically change colors to match the dominant colors of the currently playing track's album art.

Note: Ensure you have allowed the necessary permissions for your Spotify app and authenticated the first time you run the script.

Dependencies
Spotipy
Requests
Pillow (PIL)
NumPy
Scikit-learn
Disclaimer
This project is for educational purposes. Please ensure you comply with Spotify's and LIFX's terms of service when using their APIs.
