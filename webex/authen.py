import requests
import json

access_token = 'ZTA3NzBlNDAtNmU0NC00YTVlLTk0YjItMDRkODM2MzlmYmQ3YTRjNzEzMGEtMzdj_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
