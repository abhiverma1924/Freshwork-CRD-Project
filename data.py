import json

data = {}
def make_file():
  f = open('./DataBase/key_data.json',) 
  data = json.load(f) 
  return data



