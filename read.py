import json
import time
import threading
lock = threading.Lock()

def read(key):
  lock.acquire()
  #time.sleep(5)
  file = open('./DataBase/key_data.json',) 
  d = json.load(file) 
  if key not in d:
      print("ERROR: Key Does Not Exist")
  else:
      value = d[key]
      if value[1]!=0:
        if time.time()<value[1]:
          string=str(key)+":"+str(value[0])
          value = json.loads(string)
          print(value)
        else:
          del d[key]
          with open('./DataBase/key_data.json', 'w') as f:
            json.dump(d, f)
          f.close()
          print("ERROR: TTL Of The",key,"Has Expired") 
      else:
        string =str(key)+":"+str(value[0])
        print(string)
  lock.release()

