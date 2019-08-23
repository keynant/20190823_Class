import requests
import json

class Person:
    def __init__(self, d):
        self.__dict__ = d


    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

initParam = {'name' : 'Moshe', 'age' : '37', 'city' : 'Ashdod'}
r = json.loads(requests.get("https://jsonplaceholder.typicode.com/todos/5").content)

print(r)

moshe = Person(initParam)

print (moshe)


initParam = json.loads('{"name":"Keynan", "age":34, "city":"Ramat Gan"}')
keynan = Person(initParam)

print(keynan)
