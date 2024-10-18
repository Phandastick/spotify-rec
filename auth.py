# https://developer.spotify.com/dashboard/53ae987f426c4b45abc75b761d0bd49c/settings

import requests
from dotenv import dotenv_values

config = dotenv_values()

# print(config)

def getToken():
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
    
    if(res.status_code == 200):
        resJson = res.json()
        # print(resJson['access_token'])

        return resJson['access_token']
    else:
        print('Request for access token failed!')
        return 
    
# getToken()