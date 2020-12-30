# Freshwork-CRD-Project
The project is the implementation of basic operations (Create, Read, delete) on key-value data pairs. whereas, the key is supposed to be a string having not more than 32 chars and the value should be a JSON object having a max size of 16Kb stored in a JSON file of size not more than 1Gb.

Components:
Main.py - It is the main python file where all the components are imported and utilized. Also, multithreading is done.
Create.py - Create operation is executed, create function accepts a key, value and, TTL and insert the key-value pair in the JSON file while validating all the function operations required.
Read.py - Read operation is executed, return the value of the given key in the string format.
Delete.py - Delete operation is executed, delete the key-value pair from the data file, for the given key.
Data.py - Creates and loads the data present in the file into the dictionary.

Features:
Data is stored in the JSON file in the Key value pair, where the key is supposed to be a string having not more than 32 chars and the value should be a JSON object having a max size of 16Kb stored in a JSON file of size not more than 1Gb.
If the key already exists in the data, it will raise an error else it will insert the data into the JSON.
In read operation, it will return a value JSON object in the string format if the key-value exists in the data else it will raise an error.
 


   
