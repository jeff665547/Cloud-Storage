import os
os.chdir(r"C:\Users\jeff\Desktop\Learning\Python\Python IO")
# To work with JSON, we need to import JSON module.
import json

# In Python, JSON exists as a string.
p = '{"name": "Bob", "languages":["Python", "Java"]}'

# Parse 解析代碼

#%%
# 1. JSON string to Python dict.
# We can parse a JSON string using json.loads() method.
# This method returns a dictionary.
# json.loads() expects to get its text from a JSON string object.
# s in the json.loads represents string.
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(person_dict) # a dictionary
print(person)      # a JSON string

print(person_dict['languages'])

#%%
# 2. Read a JSON file
# We can use json.load() to read a file containing JSON object.
# Suppose we have a chip_info.json file which contains a JSON object.
# json.load() expects to get the text from a file-like object
with open("chip_info.json") as f:
    data = json.load(f)
    
print(data)
print(data["Info"])

#%%
# 3. Conver Python dict to a JSON string.
# We can use json.dumps() to convert a python dictionary to 
# a JSON string using json.dumps()
# s in the json.dumps represents string.
data_dict = {"name": "Bob",
             "age": 12,
             "int": 11,
             "float": 2.2,
             "True": True,
             "False": False,
             "None": None,
             "dict": {"A": 33,
                      "B": "pig"},
             "list": [1, 2, 3],
             "tuple": (1, 1, 0),
             "children": None}

#   Python    <===>     JSON
#   dict                object
#   list                array
#   tuple               array
#   str                 string
#   int, float          number
#   True                true
#   False               false
#   None                null

data_json = json.dumps(data_dict)

print(data_json)

#%%
# 4. Write JSON to a txt file.
data_dict = {"name": "Bob",
             "age": 12,
             "int": 11,
             "float": 2.2,
             "True": True,
             "False": False,
             "None": None,
             "dict": {"A": 33,
                      "B": "pig"},
             "list": [1, 2, 3],
             "tuple": (1, 1, 0),
             "children": None}

with open("person.txt", "w") as json_file:
    json.dump(data_dict, json_file)
    
#%%
# 5. Write JSON to a json file.
data_dict = {"name": "Bob",
             "age": 12,
             "int": 11,
             "float": 2.2,
             "True": True,
             "False": False,
             "None": None,
             "dict": {"A": 33,
                      "B": "pig"},
             "list": [1, 2, 3],
             "tuple": (1, 1, 0),
             "children": None}

with open("person.json", "w") as json_file:
    json.dump(data_dict, json_file, indent = 4, sort_keys = True)

#%%
# 6. Python pretty print JSON.
# Print the JSON string in a more readable format.
# Use the additional parameters indent and sort_keys 
# to json.dumps() and json.dump()
# s in the json.dumps represents string.
# If we want to save file, then using json.dump().
# json.dump() just only convert python object to a 
# JSON formatted string.
person_string = '{"name": "Bob", "languages": \
    "English", "numbers": [2, 1.6, null]}'

# Getting Pyton dictionary
person_dict = json.loads(person_string)

# Pretty Printing the JSON string back
person_json = json.dumps(person_dict, indent = 4, sort_keys = True)

print(person_json)
# 4 spaces for indentation, 
# and the keys are sorted in ascending order.
