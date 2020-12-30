import time
import json
import data
import sys

import threading
lock = threading.Lock()

d = data.make_file()
#file is loaded from the local storage and store in the dictionary

def validate(key, value):
    if key.isalpha() and len(key)<=32:# To ensure key is a string and has <= 32 char
        if sys.getsizeof(value) <= (16*1024):# To ensure the size of Value <= 16KB
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
    lock.acquire() # To ensure no other operation can use data file at the same time
    #time.sleep(5)
    # To experience threading Uncomment sleep statement
    value = convert2Json(value) # To convert value into Json Object
    if validate(key,value)== True: # Validating Key & value against tetscases
      if key in d: # check if key Already exist
        print("ERROR: This Key Already Exist")
      else:
        if sys.getsizeof(d)< (1024 * 1024 * 1024): # to ensure the size of the <= 1GB
            if timeout == 0:
                l = [value , timeout]
            else:
                l = [value, (time.time() + timeout)]
            if validateJSON(value): # checking the json object is valid or not
              d[key] = l
              print("Key Added Succesfully")
              with open('./DataBase/key_data.json', 'w') as f:
                json.dump(d, f) # Re-writting changes back to Data file 
              f.close()
            else:
              print("ERROR: Value Is Not An Valid Json Object")
        else:
            print("ERROR: Memory limit exceeded")
    else:
        print(
            "ERROR: Key Must Be A String"
        )
    lock.release() # releasing lock

