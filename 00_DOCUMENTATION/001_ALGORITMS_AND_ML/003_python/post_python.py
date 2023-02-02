# importing the requests library
# import requests
import json


with open("config.json") as json_data_file:
    data = json.load(json_data_file)

# print(data['appsync'].api_key)
# print(data)
print(data['appsync']['api_endpoint'])


input = {
        'name': 'test123',
        'description': 'some cool description'
    }

query = """
    mutation createTodo(
        $input: CreateTodoInput!
    ) {
        createTodo(input: $input){
            id
            name
            description
        }
    }
"""

# r = requests.post(API_ENDPOINT, json={'query': query})
# print(r.status_code)
# print(r.text)