import requests
import base64
url = 'http://118.190.210.225:8800/v2/users/55/behavior?$user_id=7985713-e809edeec7a73f1ff7f1fb964e2023e0e1e81d2cf26d1b64b4db13d434aef2b06cc7a5aab423cdb0a57a25ad63441237'
url2 = 'http://118.190.210.225:8800/v2/users/55/behavior?$user_id=7985713-e809edeec7a73f1ff7f1fb964e2023e0e1e81d2cf26d1b64b4db13d434aef2b06cc7a5aab423cdb0a57a25ad63441237'
username = 'admin'
pw = 'youliwang164ca6ccc25'

headers = {'Authorization': 'Basic ' + (base64.b64encode((username + ':' + pw).encode('utf-8'))).decode('utf-8')}
print(headers)
resp = requests.get(url2, headers=headers)
print(resp.content)