# use delete
# use delete method of api

import requests
import json
import jsonpath
#api url
url = "https://reqres.in/api/users/page=2"
#send get request

response = requests.delete(url)
print(response.status_code)
assert response.status_code
