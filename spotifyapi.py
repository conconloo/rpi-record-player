import time
import configparser
from requests.models import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# READ CONFIG FILE
config = configparser.ConfigParser(allow_no_value=True)
config.read("config.cfg")
learn_card_uid = config["UIDS"]["learn_card_uid"]
default_volume = int(config["DEVICE"]["default_volume"])

playstate = False

# AUTHENTICATION WITH SPOTIPY
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config["AUTH"]["client_id"],
        client_secret=config["AUTH"]["client_secret"],
        redirect_uri=config["AUTH"]["redirect_uri"],
        scope=config["AUTH"]["scope"],
        open_browser=False
    )
)

# FUNCTIONS
# returns URI of album or playlist that the track is currently being played from
def curr_playback():
  playback = sp.current_playback()
  if playback != None:
    try:
      return [
          playback["context"]["uri"],
          playback["item"]["name"],
          playback["item"]["artists"][0]["name"],
      ]
    except TypeError:  # Personal playlists cant be learned that easy. WIP
      return -1
  else:
    return -1
    
def start_playing(uri):
  try:
    sp.start_playback(context_uri=uri)
  except:
    print('error playing song')
    return -1