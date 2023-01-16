import pyrebase
import random
import time

config = {
  "apiKey": "AIzaSyBfsvZlYsWXbCGCtDw6jKvx71liCHHeRgI",
  "authDomain": "daq-smart-home.firebaseapp.com",
  "databaseURL": "https://daq-smart-home-default-rtdb.firebaseio.com/",
  "storageBucket": "daq-smart-home.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

while True:
    data = {
    "Temp" : random.randrange(5, 15),
    "No-of-Human" : random.randrange(0, 5)
    }

    # db.child("Status").push(data)

    # db.child("Status").child("DAQ").update(data)
    db.update(data)
    print(data)
    print("data_send")
    user1 = db.child("LED").get()
    LED = user1.val()
    user2 = db.child("Fan").get()
    Fan = user2.val()
    print(LED, Fan)
    db.child("Status").remove()
    time.sleep(1)
