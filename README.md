The project is the implementation of basic operations (Create, Read, delete) on key-value data pairs. whereas, the key is supposed to be a string having not more than 32 chars and the value should be a JSON object having a max size of 16Kb stored in a JSON file of size not more than 1Gb.

# Components:
1. Main.py - It is the main python file where all the components are imported and utilized. Also, multithreading is done.
2. Create.py - Create operation is executed, create function accepts a key, value and, TTL and insert the key-value pair in the JSON file while validating all the function operations required.
3. Read.py - Read operation is executed, return the value of the given key in the string format.
4. Delete.py - Delete operation is executed, delete the key-value pair from the data file, for the given key.
5. Data.py - Creates and loads the data present in the file into the dictionary.

# Features:
* Data is stored in the JSON file in the Key value pair, where the key is supposed to be a string having not more than 32 chars and the value should be a JSON object having a max size of 16Kb stored in a JSON file of size not more than 1Gb.
* If the key already exists in the data, it will raise an error else it will insert the data into the JSON.
* In the read operation, it will return a value JSON object in the string format if the key-value exists in the data else it will raise an error.
* In the delete operation, It will delete the key-value pair from the data file if the key exists in the data file else it will raise an error.
* Every key has time to live (TTL), after the TTL the key value is not available for any read and delete operation.
* If the value data is not a valid JSON object it will give an error.
* Multiple users can use crd operation at a time. 
* An optimized multithreading technique is used with thread safety is maintained. Only one operation can use the resource at a time maintaining the synchronization. 
* We were able to maintain good performance and search complexity of O(N), create complexity of O(1) and delete complexity of O(N). 
 


 


   


