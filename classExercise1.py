import requests
import json

class ToDo:
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

rawTodos = requests.get("https://jsonplaceholder.typicode.com/todos")
contentTodos = json.loads(rawTodos.content)
todoList = []

for d in contentTodos:
    if d['id'] < 10:
        todoList.append(d['title'])


print(todoList)
