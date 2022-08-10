#UPDATE  resource on server
#use PUT method
#steps:-
#1.read input json using file
#2.parse into json format
#3.hit put method
#4.parse response to json format
#5.validate response
import jsonpath
import requests
import json
#api url
url = "https://reqres.in/api/users/2"

file= open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\creatnew.txt', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
#make put request with json body
response = requests.put(url, requests_json)
#validate response code
assert response.status_code == 200

#parse response to json format
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updateAt')
print(updated_li)