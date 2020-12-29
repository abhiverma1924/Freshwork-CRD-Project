import time
import json
import data
import sys
d = data.make_file()

def validate(key, value):
    if type(key) == str and len(key) <= 32:
        if sys.getsizeof(value) <= (16*1024):
            return True
        else:
            return False
    else:
        return False

def create(key, value, timeout=0):
    value = json.dumps(value)
    if validate(key,value)== True:
      if key in d:
        print("error: this key already exists")
      else:
        if len(d) < (1024 * 1020 * 1024):
            if timeout == 0:
                l = [value, timeout]
            else:
                l = [value, time.time() + timeout]
            if len(key) <= 32:
                d[key] = l
                print("key added succesfully")
                #print(d)
                with open('./DataBase/key_data.json', 'w') as f:
                  json.dump(d, f)
                f.close()
        else:
            print("error: Memory limit exceeded!! ")
    else:
        print(
            "error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers"
        )
