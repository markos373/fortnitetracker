import requests
import json
import matplotlib.pyplot as plt
import time
def print_match(match):
    print("Match count: ", match['matches'], "\nKDA: ", round(match['kills']/match['matches'],2))
    time_info = match['dateCollected'].split("T")
    print("Match date: ", time_info[0], "\nMatch time: ", time_info[1], "\n************")
name = input("input name of user: ")
url = "https://api.fortnitetracker.com/v1/profile/pc/" + name
r=requests.get(url, headers={'TRN-Api-Key': 'b46c80e9-ee91-4aea-bc41-dc15f96f7c4a'})
json_data = json.loads(r.text)
prev_ids = []
detected = False
for i in range(1):
    kds = []
    for match in json_data['recentMatches']:
        kds.append(round(match['kills']/match['matches'],2))
        if(match['id'] not in prev_ids):
            print_match(match)
        prev_ids.append(match['id'])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    nums = [1,2,3,4,5,6,7,8,9,10]
    plt.plot(nums,kds)
    for xy in zip(nums, kds):
        ax.annotate(xy[1], xy=xy, textcoords='data')
    plt.ylabel('K/D')
    plt.xlabel('Recent Match #')
    plt.show()
