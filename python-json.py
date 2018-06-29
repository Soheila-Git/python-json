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

data = json.loads(people_string)
print(data)
