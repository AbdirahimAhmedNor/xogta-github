import requests
import json
import sys
from longestStreak import get_longest_streak

username = sys.argv[1]
token = sys.argv[2]

def getUserInfo(username, token):
  user_info_url = f"https://api.github.com/users/{username}"
  contribution_url = f"https://corsanywhere.herokuapp.com/https://github-contributions-api.deno.dev/{username}.json"
  
  HEADERS = {'Authorization': 'bearer {}'.format(token)}

  user_info_response = requests.get(user_info_url, auth=(username, token))
  number_contribution_response = requests.get(contribution_url)

  user_info_result = json.loads(user_info_response.text)
  number_contribution_result = json.loads(number_contribution_response.text)

  # Getting the information from the json
  name = user_info_result['name']
  public_repos = user_info_result['public_repos']
  total_private_repos = user_info_result['total_private_repos']
  total_contributions = number_contribution_result['totalContributions']
  longest_streak = get_longest_streak(number_contribution_result)

  print()
  print()
  print()
  print(" 🤵 Magaca:".rjust(20), name)
  print()
  print(" 🏗  keydadka".rjust(22), 'banaanka:', public_repos) 
  print()
  print(" 🔒 keydadka".rjust(21)," qaaska:", total_private_repos)
  print()
  print(" 🚧 Tirada".rjust(20)," wax ku biirin:", total_contributions)
  print()
  print(" ⚾️🚴🥎 Longest".rjust(23)," streak:", longest_streak)
  print()
  print()
  print()


getUserInfo(username, token)

