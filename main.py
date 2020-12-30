import create as cr
#importing create operation 
import read as r
#importing read operation 
import delete as dl 
#importing delete operation 
#import json
import threading
#importing module for threading
lock = threading.Lock()
#Lock to deal with the race around conditions. Lock is implemented using a Semaphore object provided by the Operating System.

if __name__ == "__main__":
  threads = list()
  #list of thread is created
  i = -1
 
  data_created = threading.Thread(target=cr.create, args=('Lata',{"nikhil": "kumar","akash": 5, "manjeet": 10, "akshat": 15}, 0,))
  #For data creation thread is created
  #Key Should be string else it will give an error   
  #Value should be Json object else it will give an error
  data_read = threading.Thread(target=r.read, args= ('Lata',))
  #For reading data thread is created
  data_delete = threading.Thread(target=dl.delete, args= ('Abhi',))
  #For Delting data thread is created
  threads.append(data_created)
  threads.append(data_read)
  threads.append(data_delete)
  #appending all the operation in the thread list
  data_created.start()
  data_read.start()
  data_delete.start()
  #To start a thread,
 
for thread in threads:
  thread.join()
  #In order to stop execution of current program until a thread is complete, we use join method. 
