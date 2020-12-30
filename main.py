import create as cr
import data as d
import read as r
import delete as dl 
#import json
import threading
lock = threading.Lock()


if __name__ == "__main__":
  
  threads = list()
  i = -1
  while(i!=1):
    data_created = threading.Thread(target=cr.create, args=('hema',{"nikhil": 2,"akash": 5, "manjeet": 10, "akshat": 15}, 0,))
    data_read = threading.Thread(target=r.read, args= ('hema',))
    data_delete = threading.Thread(target=dl.delete, args= ('Abhinav',))
    threads.append(data_created)
    threads.append(data_read)
    threads.append(data_delete)
    data_created.start()
    data_read.start()
    data_delete.start()
    i=1

for thread in threads:
  thread.join()