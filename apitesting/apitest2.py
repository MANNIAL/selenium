# fecth response content
# json path
import requests
import json
import jsonpath
#api url
url = "https://reqres.in/api/users/page=2"
#send get request

response = requests.get(url)
#json response
json_response= json.loads(response.text)
print(json_response)
# fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
# or
#assert pages[0] == 4
