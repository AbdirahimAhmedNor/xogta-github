import requests
import json
import sys

username = sys.argv[1]
token = sys.argv[2]

def getUserInfo(username, token):
  url = f"https://api.github.com/users/{username}"
  HEADERS = {'Authorization': 'bearer {}'.format(token)}

  with requests.Session() as s:
    s.headers.update(HEADERS)
    response = s.get(url)
    result = json.loads(response.text)

    name = result['name']
    public_repos = result['public_repos']
    total_private_repos = result['total_private_repos']

    print(name, total_private_repos, public_repos)


getUserInfo(username, token)
