# Spotify Album Art Color Sync with LIFX Lights

This Python script dynamically changes the colors of your LIFX lights based on the dominant colors of the currently playing Spotify track's album art. It uses the Spotify API to fetch the current track information and the album art image. The dominant colors are extracted using KMeans clustering provided by scikit-learn. These colors are then converted to the HSB color model, which is compatible with LIFX lights, to set the light colors accordingly.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running the Script](#running-the-script)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A more detailed introduction to the project. Explain what problems it solves and how it can be useful.

## Features

List of the standout features of the project.

## Setup

1. Spotify API: You need to have a Spotify Developer account to create an app and get your Client ID and Client Secret. Also, set the Redirect URI to http://localhost:8000.
2. LIFX Token: Generate a LIFX token from the LIFX Cloud HTTP API to control your lights.
3. Python Libraries: This script requires spotipy, requests, PIL, numpy, scikit-learn, and a few other libraries. Make sure to install these dependencies.

## Prerequisites

Before you can run the script, you need to have Python and `pip` installed on your system. Once you have Python and `pip` set up, you can install the following libraries required by the project:

```bash
# Install Spotipy for interacting with the Spotify Web API
pip install spotipy

# Install Requests for making HTTP requests
pip install requests

# Install Pillow (PIL Fork) for image processing tasks
pip install Pillow

# Install NumPy for numerical computing
pip install numpy

# Install Scikit-learn for machine learning and data mining
pip install scikit-learn

