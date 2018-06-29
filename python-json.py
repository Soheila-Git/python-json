'''
Based on Youtube video:
Python Tutorial: Working with JSON Data using the json Module
By Corey Schafer
https://www.youtube.com/watch?v=9N6a-VLBa2I
'''
import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "616-555-7187",
      "emails": ["johnsmith@gmail.com", "jsmith@work.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "543-453-5544",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

# Load JSON to Python object
data = json.loads(people_string)

print(data)
'''
{'people': [{'name': 'John Smith', 'phone': '616-555-7187', 'emails':
['johnsmith@gmail.com', 'jsmith@work.com'], 'has_license': False},
{'name': 'Jane Doe', 'phone': '543-453-5544', 'emails': None,
'has_license': True}]}
'''

print(type(data))
# <class 'dict'>


print(type(data['people']))
# <class 'list'>

# Access each person
for person in data['people']:
  print(person)
'''
{'name': 'John Smith', 'phone': '616-555-7187', 'emails': ['johnsmith@gmail.com', 'jsmith@work.com'], 'has_license': False}
{'name': 'Jane Doe', 'phone': '543-453-5544', 'emails': None, 'has_license': True}
'''
