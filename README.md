# rpi-record-player
CSCE 462 Final Project

Spring 2022

Connie Liu, Katelyn Yim, and Roshin Lal

## Intro
This is a github repo for a Raspberry Pi Record Player. This Record Player uses RFID and NFC tokens to control playback of Spotify tracks/playlists.

## Dependencies
This project runs on Raspotify, a Spotify Connect client. Download and install here: https://github.com/dtcooper/raspotify

You also need to create a new Spotify app on https://developer.spotify.com/ with a Spotify Developer account. Copy/paste the Client ID and Secret into the config.cfg file.

## First-Time Setup & Configuration
Run check_card.py via command terminal to scan the learn card, play/pause card, and skip card UIDs.
```bash
python3 check_card.py
```
Copy/paste the corresponding card UIDs into the config.cfg file.

Start a Spotify session on a device that is connected to the same Wifi network as your Raspberry Pi. Select your Raspberry Pi as the playback device as you have configured it on Raspotify installation.

Create the cardList.csv file via command terminal:
```bash
touch cardList.csv
```

Your Raspberry Pi should now be good to go! Run the following command to start a new session:
```bash
python3 main.py
```

## Credits
RFID & NFC technology was configured and implemented with the following tutorial: https://www.raspberrypi.com/news/read-rfid-and-nfc-tokens-with-raspberry-pi-hackspace-37/

Spotify Authentication as well as helpful code for config.cfg, rfidcommunication.py, spotifyapi.py, and main.py was completed from this article: https://www.instructables.com/RFID-Spotify-Jukebox/

Mapping of card UIDs and Spotify URIs was done with help from this article: https://fsahli.wordpress.com/2015/11/02/music-cards-rfid-cards-spotify-raspberry-pi/

Spotipy API documentation: https://spotipy.readthedocs.io/en/2.13.0/
