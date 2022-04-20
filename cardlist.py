"""
This file takes care of the csv file to keep track of card UIDs
and their corresponding Spotify URIs.
"""

import csv
import os.path
import sys

class CardList:
  def __init__(self):
    self.path = os.path.dirname(os.path.realpath(__file__))
    self.cardList = self.readList()
    
  # read cardlist.csv
  def readList(self):
    with open(self.path + '/cardList.csv', mode='r') as infile:
      reader = csv.reader(infile)
      cardList = {rows[0]:rows[1] for rows in reader}
      infile.close()
    return cardList
  
  # return playlist uri of card if it exists, prints error if not
  def getPlaylist(self,card):
    self.cardList = self.readList()
    try:
      return self.cardList[card]
    except:
      print('Card %s is not card list' % card)
      return -1
  
  # add card uid and playlist uri to cardlist.csv if card does not exist
  def addPlaylist(self, card, plist):
    print("Checking card...")
    try:
      if card not in self.cardList.keys():
        f = open(self.path + '/cardList.csv', 'a')
        f.write(card + ',' + plist + '\n')
        self.cardList[card] = plist
        return 1
      else:
        print('Card %s is already being used. Please restart with a different card.' % card)
        return -1
    except:
      print('Could not write file')
      if not os.path.isfile(self.path + '/cardList.csv'):
        print('File cardList.csv does not exist')