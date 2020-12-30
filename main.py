import create as cr
#import data as d
import read as r
#import delete as dl 
import json

cr.create('NehaCOOL', {'nikhil': 1, 'akash' : 5, 'manjeet' : 10, 'akshat' : 15}, 0)
str = r.read('Abhinav')
print(str)
print(type(str))