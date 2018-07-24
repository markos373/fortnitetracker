import requests
import json
r=requests.get("https://api.fortnitetracker.com/v1/profile/pc/squid111", headers={'TRN-Api-Key': 'b46c80e9-ee91-4aea-bc41-dc15f96f7c4a'})
json_data = json.loads(r.text)
print(len(json_data['recentMatches']))
