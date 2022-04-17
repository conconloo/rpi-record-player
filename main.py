from time import sleep, time
import sys
import spotifyapi as spotify
import rfidcommunication as rfid

def main():
  while True:
    if(rfid.detect_learn_card()):
      if(write_card()==-1):
        print('error writing new card. please try again')
    else:
      uri = rfid.read_uri()
      if uri == -1:
          print("Make sure you already added this Card.")
          sleep(1)
          continue
  
      print("Found Music-Card.")
      if spotify.start_playing(uri) == -1:  # play uri playlist at device
          print("Current device unavailable, please select an available device.")  # maybe use fallback device?
          print("This can happen if you use a Phone or PC that is not always online.")
          sleep(1)
          continue
  
      print("Playing now!")
      spotify.playstate = True
      sleep(1)
    
def write_card():
  try:
    current = spotify.curr_playback()
  except TypeError:
    print(
        """
    >Please play a track out of the playlist you want to learn.
    >Can't be \"Liked Songs\" or Podcast-Shows.
    >Aborting Learning.
    """
    )
    return -1
  print("")
  print("Playing a playlist containing: {}, by {}.".format(current[1], current[2]))
  uri = current[0]
  
  sleep(3)
  print("Please scan the card you would like to write to.")
  str_uid = rfid.check_uid()[1]
  if(rfid.detect_learn_card()):
    print("cannot write to learn card. aborting.")
    return -1
  else:
    print('detected card with uid: ', str_uid)
    if(rfid.write_uri(uri) == -1):
      return -1
  
  print('card with uid: ', str_uid, ' learned uri: ', uri, ' successfully!')
  
if __name__ == "__main__":
  while True:
    try:
      main()
    except:
      print("CRASHED!")
      sys.exit()