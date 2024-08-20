import requests
import json

access_token = 'ZTA3NzBlNDAtNmU0NC00YTVlLTk0YjItMDRkODM2MzlmYmQ3YTRjNzEzMGEtMzdj_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
}
params = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0', 'max': 10}
res = requests.get(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4, ensure_ascii=False).encode('utf8').decode()) 
