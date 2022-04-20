import time
import configparser
from cardlist import CardList
import RPi.GPIO as GPIO
from pn532 import *

cards = CardList()

# READ CONFIG FILE
config = configparser.ConfigParser(allow_no_value=True)
config.read("config.cfg")
learn_card_uid = config["UIDS"]["learn_card_uid"]
pause_card_uid = config["UIDS"]["pause_card_uid"]
skip_card_uid = config["UIDS"]["skip_card_uid"]

def check_uid():
  try:
    # Configure PN532 to communicate with MiFare cards
    pn532 = PN532_UART(debug=False, reset=20)
    pn532.SAM_configuration()

    while True:
      # Check if a card is available to read
      uid = pn532.read_passive_target(timeout=0.5)
      # Try again if no card is available.
      if uid is None:
          continue
      str_uid = "".join(format(x, "0x") for x in uid)
      return uid, str_uid
  except Exception as e:
    print(e)
  finally:
    GPIO.cleanup()
  
def detect_card():
  uid, str_uid = check_uid()
  if(str_uid == learn_card_uid):
    return 1
  elif(str_uid == pause_card_uid):
    return 2
  elif(str_uid == skip_card_uid):
    return 3
  else:
    return -1
    
def write_uri(uri):
  uid, str_uid = check_uid()
  if(cards.addPlaylist(str_uid, uri) == -1):
    return -1
  else:
    print("Writing card...")
    return 1

def read_uri():
  uid, str_uid = check_uid()
  plist = cards.getPlaylist(str_uid)
  #print('playlist detected: ', plist)
  if plist != '':
    return plist
  else:
    return -1
