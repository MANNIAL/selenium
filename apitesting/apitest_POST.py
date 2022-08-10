#creat new resource on server
#use post method
#steps:-
#1.read input json using file
#2.parse into json format
#3.hit post method
#4.parse response to json format
#5.validate response
import jsonpath
import requests
import json
#api url
url = "https://reqres.in/api/users/page=2"

file= open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\creatnew.txt','r')
json_input = file.read()
requests_json = json.loads(json_input)

print(requests_json)
#make post request with json bady
response = requests.post(url,requests_json)
#print(response.content)
#validate response content
assert response.status_code == 201
#fetch header from response
print(response.headers.get('content-length'))
#parse response to json format
response_json= json.loads((response.text))
id = jsonpath.jsonpath(response_json,'id')
print(id[0])#different id's are stored

