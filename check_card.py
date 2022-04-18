import rfidcommunication as rfid

while True:
  uid, str_uid = rfid.check_uid()
  print('card: ', str_uid)