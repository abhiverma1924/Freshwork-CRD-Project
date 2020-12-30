import json

def make_file():
  f = open('./DataBase/key_data.json',) # file path
  data = json.load(f) 
  return data




