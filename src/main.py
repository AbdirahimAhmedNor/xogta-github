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

    print()
    print()
    print()
    print(" 🤵 Magaca:".rjust(20), name)
    print()
    print(" 🏗  keydadka".rjust(22), 'banaanka:', public_repos) 
    print()
    print(" 🔒 keydadka".rjust(21)," qaaska:", total_private_repos)
    print()
    print()
    print()


getUserInfo(username, token)
