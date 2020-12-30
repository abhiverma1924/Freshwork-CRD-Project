import json
import time
def delete(key):
    file = open('./DataBase/key_data.json',) 
    d = json.load(file) 
    if key not in d:
        print("ERROR: Key Does Not Exist") 
    else:
        b = d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("Key Successfully Deleted")
            else:
                print("ERROR: TTL Of The",key,"Has Expired") 
        else:
            del d[key]
            with open('./DataBase/key_data.json', 'w') as f:
              json.dump(d, f)
            f.close()
            print("Key Deleted Successfully")
