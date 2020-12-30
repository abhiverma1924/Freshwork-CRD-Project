import data
import json
import time
import threading
lock = threading.Lock()
def delete(key):
    lock.acquire()  # To ensure no other operation can use data file at the same time
    #time.sleep(5) 
    # To experience threading Uncomment sleep statement
    d = data.make_file() #file is loaded from the local storage and store in the dictionary
    if key not in d:
        print("ERROR: Key Does Not Exist") 
    else:
        value = d[key]
        if value[1]!=0:
            if time.time()<value[1]: ## checking for TTL
                del d[key] # delete key
                print("Key Successfully Deleted")
            else:
              del d[key]
              with open('./DataBase/key_data.json', 'w') as f:
                json.dump(d, f)# Re-writting changes back to Data file
              f.close()
              print("ERROR: TTL Of The",key,"Has Expired") 
        else:
            del d[key]
            with open('./DataBase/key_data.json', 'w') as f:
              json.dump(d, f) # Re-writting changes back to Data file
            f.close()
            print("Key Deleted Successfully")
    lock.release()# releasing resource 
