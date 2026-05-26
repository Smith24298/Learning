"""
json module:
"""

import json

x =  '{ "name":"John", "age":30, "city":"New York"}' # this is json object

y = json.loads(x)
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
} # this is python object

y=json.dumps(x)
print(y)

"""
You can convert Python objects of the following types, into JSON strings:

    dict --> object
    list --> array
    tuple --> array
    string --> string
    int --> number
    float --> number
    True --> true
    False --> false
    None --> null    

"""

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4,separators=(". ", " = "))) # the indent parameter is used to specify the number of spaces to use for indentation in the output JSON string. The separators parameter is used to specify the separators to use between items in the output JSON string. The default separators are (', ', ': '), which means that items will be separated by a comma and a space, and key-value pairs will be separated by a colon and a space. In this example, we have changed the separators to ('. ', ' = '), which means that items will be separated by a period and a space, and key-value pairs will be separated by an equals sign and a space.




"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""
