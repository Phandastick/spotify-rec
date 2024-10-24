import json

with open('log.json', 'r') as f:
    data = json.load(f)
    
    for i in data['tracks']:
        print("Song:", i['name'])
        print("Artist Name:", i['artists'][0]['name'] + '\n')
