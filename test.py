# https://developer.spotify.com/dashboard/53ae987f426c4b45abc75b761d0bd49c/settings

import requests
import json
from dotenv import dotenv_values

config = dotenv_values()

# print(config)

def getAuth():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': config['CLIENTID'],
        'client_secret': config['CLIENTSECRET']
    }

    res = requests.post(url=url,
                data=data,
                headers=headers)
    
    res

    resJson = json.loads(res.content)
    
    return resJson['access_token']

print(getAuth())