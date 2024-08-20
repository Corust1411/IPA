import requests
import json

access_token = 'NWUxYTZlYjctN2JmYS00YzkxLTg4OTUtOTYwZjEwNWI0N2QzM2ZlMzEzZjgtNzMw_P0A1_1ad92174-dfe2-4740-b008-57218895946c'
url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi',  # Replace with your room ID
    'max': 10  
}

res = requests.get(url, headers=headers, params=params)


response_json = res.json()
print(json.dumps(response_json, indent=4, ensure_ascii=False).encode('utf8').decode())
