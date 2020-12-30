import time
import json
import data
import sys
import threading
lock = threading.Lock()
d = data.make_file()

def validate(key, value):
    if key.isalpha() and len(key)<=32:
        if sys.getsizeof(value) <= (16*1024):
            return True
        else:
            print("ERROR: Size Of Value Is More Than 16KB")
            return False
    else:
        print("ERROR: Length Of The String Should Be Less Than 32 Char")
        return False

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def convert2Json(value):
  if(type(value)==dict):
    value = json.dumps(value, indent = 4) 
    return value
  else:
    print("ERROR: Value Is Not Json Object- We Only Accept Json object As A value.")


def create(key, value, timeout=0):
    lock.acquire()
    #time.sleep(5)
    value = convert2Json(value)
    if validate(key,value)== True:
      if key in d:
        print("ERROR: This Key Already Exist")
      else:
        if len(d) < (1024 * 1024 * 1024):
            if timeout == 0:
                l = [value , timeout]
            else:
                l = [value, (time.time() + timeout)]
            if validateJSON(value):
              d[key] = l
              print("Key Added Succesfully")
              with open('./DataBase/key_data.json', 'w') as f:
                json.dump(d, f)
              f.close()
            else:
              print("ERROR: Value Is Not An Valid Json Object")
            #else:
            #  print("ERROR: Length Of The String Should Be Less Than 32 Char")
        else:
            print("ERROR: Memory limit exceeded")
    else:
        print(
            "ERROR: Key Must Be A String"
        )
    lock.release()

