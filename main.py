from time import sleep, time
import sys
import spotifyapi as spotify
import rfidcommunication as rfid

def main():
  
  print("Welcome to the Raspberry Pi Spotify Record Player!")
  print("To start, please make sure the following are true:")
  print("(1) You are using a Spotify Premium account")
  print("(2) The Raspberry Pi is connected to the same WiFi network as an existing Spotify device")
  print("(3) The Raspberry Pi has been selected as the playback device for your Spotify Connect")
  print("Scan cards to begin. Happy listening!")
  print("")
  
  while True:
    command = rfid.detect_card()
    if(command == 1):
      print("Learn card detected - writing process initiated.")
      if(write_card()==-1):
        print("There was an error writing this card. Please try again.")
        print("")
      else:
        continue
      sleep(1)
    elif(command == 2):
      try:
        spotify.playpause()
        sleep(1)
        print_playback()
      except:
        print("There was an error playing/pausing. Please try again.")
        print("")
    elif(command == 3):
      try:
        spotify.skip_track()
        sleep(1)
        print_playback()
      except:
        print("There was an error skipping this track. Please try again.")
        print("")
    else:
      uri = rfid.read_uri()
      if uri == -1:
        print("Make sure you already added this Card.")
        print("")
        sleep(1)
        continue
      else:
        print("Found Music-Card.")
        if spotify.start_playing(uri) == -1:  # play uri playlist at device
            print("Current device unavailable, please select an available device.")  # maybe use fallback device?
            print("This can happen if you use a Phone or PC that is not always online.")
            sleep(1)
            continue
        
        sleep(1)
        print_playback()
        sleep(1)
        
def print_playback():
  try:
    curr_track = spotify.curr_playback()
  except TypeError:
    print(">Please play a track out of the playlist you want to learn.")
    print(">Can't be \"Liked Songs\" or Podcast-Shows.")
    print(">Aborting Learning.")
    return -1
  print("{} by {}.".format(curr_track[1], curr_track[2]))
  print("")
  return curr_track
    
def write_card():
  print("Preparing to write playlist with song:")
  curr_track = print_playback()
  uri = curr_track[0]
  
  sleep(2) # prevent double-reading of previous card
  print("Please scan the card you would like to write to.")
  str_uid = rfid.check_uid()[1]
  check_card = rfid.detect_card()
  if(check_card == -1):
    if(rfid.write_uri(uri) == -1):
      return -1
    else:
      print('Card with uid: ', str_uid, ' learned uri: ', uri, ' successfully!')
      print("")
      return 1
  else:
    print("Cannot write to preset card. Aborting.")
    return -1
  
if __name__ == "__main__":
  while True:
    try:
      main()
    except:
      print("CRASHED!")
      sys.exit()