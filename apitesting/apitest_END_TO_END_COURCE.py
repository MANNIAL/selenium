# add new student
# add technical skills
# add address
# fetch complete detaile
import requests
import json
import jsonpath


def test_api():
    app_url = "https://thetestingworldapi.com/api/studentsDetails"
    fun = open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\new 3.txt', 'r')
    requests_json = json.loads(fun.read())
    response = requests.post(app_url, requests_json)
    print(response.text)
    idn = jsonpath.jsonpath(response.json(), 'id')
    print(idn[0])
    # def test_tech_apitest():

    tech_url = "https://thetestingworldapi.com/api/technicalskills"
    fun = open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\tech_api.txt', 'r')
    requests_json = json.loads(fun.read())
    resquest_json['id']= int(id[0])
    resquest_json['std_id'] = id[0]
    response = requests.post(tech_url, requests_json)
    print(response.text)


    add_url = "https://thetestingworldapi.com/api/addresses"
    fun = open('C:\\Users\\kramk\\OneDrive\\Desktop\\New folder\\add_api.txt', 'r')
    requests_json = json.loads(fun.read())
    resquest_json['std_id']= id[0]
    response = requests.post(add_url, requests_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/ api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)
