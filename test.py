import requests
import base64
url = 'http://118.190.210.225:8800/v2/users/55/behavior?$user_id=7985713-e809edeec7a73f1ff7f1fb964e2023e0e1e81d2cf26d1b64b4db13d434aef2b06cc7a5aab423cdb0a57a25ad63441237'
url2 = 'http://118.190.210.225:8800/v2/users/55/behavior?$begin_day=2017-10-15&$end_day=2017-10-27&$user_id=7985713-e809edeec7a73f1ff7f1fb964e2023e0e1e81d2cf26d1b64b4db13d434aef2b06cc7a5aab423cdb0a57a25ad63441237'
url3 = 'http://118.190.210.225:8800/v2/users/55/behavior?%24user_id=323520-d80987d9942577853332ff5a69023e8309f540963f6876af233e92581114d220990ee3df813d4bfb97a61b3d871c85a5&%24begin_day=2017-12-06&%24end_day=2017-12-10'
url4 = 'http://118.190.210.225:8800/v2/users/55/behavior?$user_id=2452121-78011b5a6228e4bb77df4422d75edc70d1767d259cac94d22de4f986cee2ca8a0cf42988774c4bda39f912cb810cd188&$begin_day=2017-12-06&$end_day=2017-12-10'
url5 = 'http://118.190.210.225:8800/v2/users/55/behavior?$user_id=5067934-fed9a7408220ccc3e511dd6c31c1f8f004c3ddde6a060b242ba5b292d4daedda580c017753c1289d448e171e29c4b020'
url6 = 'http://118.190.210.225:8800/v2/users/55/behavior?%24user_id=2452121-78011b5a6228e4bb77df4422d75edc70d1767d259cac94d22de4f986cee2ca8a0cf42988774c4bda39f912cb810cd188'
username = 'admin'
pw = 'youliwang164ca6ccc25'

headers = {'Authorization': 'Basic ' + (base64.b64encode((username + ':' + pw).encode('utf-8'))).decode('utf-8')}
print(headers)
resp = requests.get(url6, headers=headers)
print(resp.content.decode('utf-8'))