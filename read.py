import json
import time

def read(key):
  file = open('./DataBase/key_data.json',) 
  d = json.load(file) 
  if key not in d:
      print("ERROR: Key Does Not Exist")
  else:
      value = d[key]
      if value[1]!=0:
        if time.time()<value[1]:
          stri=str(key)+":"+str(value[0])
          value = json.loads(stri)
          return value
        else:
          print("ERROR: TTL Of The ",key,"Has Expired") 
      else:
        stri=str(key)+":"+str(value[0])
        return stri
