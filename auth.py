# https://developer.spotify.com/dashboard/53ae987f426c4b45abc75b761d0bd49c/settings

import requests
from dotenv import dotenv_values

config = dotenv_values()

# print(config)

def getToken(choice):
    choice = choice.split(',')
    authType = ""
    scope = ""
    
    if(len(choice)> 1):
        authType = choice[0]
        scope = choice[1]
    else:
        authType = choice[0]
    

    if(authType == 'Client Credentials'):
        token = clientCredentials()
    elif (authType == 'Authorization Code'):
        token = authorizationCode(scope)
    else:
        print('auth.py> Invalid Choice!')

    return token

def clientCredentials():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials', 
        'client_id': config['CLIENT_ID'],
        'client_secret': config['CLIENT_SECRET']
    }

    res = requests.post(url=url,
                data=data,
                headers=headers)
    
    if(res.status_code == 200):
        resJson = res.json()
        # print(res.text)

        return resJson['access_token']
    else:
        print('auth.py> Request for access token failed!')
        return 
    
def authorizationCode(scope):
    print('auth.py> Getting auth code...')
    url = 'https://accounts.spotify.com/authorize'
    client_id = config['CLIENT_ID']
    response_type = 'code'
    redirect_url = 'http://localhost:5000/home'

    params = {
        'client_id': client_id,
        'response_type': response_type,
        'redirect_uri': redirect_url,
        'scope': scope
    }

    res = requests.get(
        url=url,
        params=params
    )

    return res

# print(getToken())
# print(getToken('Client Credentials'))