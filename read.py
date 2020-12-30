import json
import data 
import time

import threading
lock = threading.Lock()

def read(key):
  lock.acquire()# To ensure no other operation can use data file at the same time
  #time.sleep(5)
  # To experience threading Uncomment sleep statement
  d = data.make_file()
  #file is loaded from the local storage and store in the dictionary
  if key not in d:
      print("ERROR: Key Does Not Exist")
  else:
      value = d[key]
      if value[1]!=0:
        if time.time()<value[1]: # Checking For TTL 
          string=str(key)+":"+str(value[0])
          value = json.loads(string)
          print(value)
        else:
          print("ERROR: TTL Of The",key,"Has Expired")
      else:
        string =str(key)+":"+str(value[0])
        print(string)
  lock.release() # resource released

