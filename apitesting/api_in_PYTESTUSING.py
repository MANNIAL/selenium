#CONVERT TESTCASE INTO PYTEST FORMAT
#EXCUTE TESTCASE BY USING PYTHON
#WRITE MULTIPLE TESTCASE IN FILE
import requests
import json
import jsonpath
import pytest
#api url
url = "https://reqres.in/api/users"
def test_pytestinapi():
    file= open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\creatnew.txt','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    print(requests_json)
    response = requests.post(url, requests_json)
    assert response.status_code == 201
    print(response.headers.get('content-length'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0]) #different id's are stored
def test_userother_pytestinapi():
    file= open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\creatnew.txt','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    print(requests_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0]) #different id's are stored

