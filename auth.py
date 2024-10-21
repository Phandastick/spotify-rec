# https://developer.spotify.com/dashboard/53ae987f426c4b45abc75b761d0bd49c/settings

import requests
import base64
from dotenv import dotenv_values
import urllib

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
        token = getClientCredentials()
    elif (authType == 'Authorization Code'):
        token = getAuthorizationCode(scope)
    else:
        print('auth.py> Invalid Choice!')

    return token

def getClientCredentials():
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
    
def getAuthorizationCode(scope):
    print('auth.py> Getting auth code...')
    url = 'https://accounts.spotify.com/authorize'
    client_id = config['CLIENT_ID']
    response_type = 'code'
    redirect_url = 'http://127.0.0.1:5000/callback'

    params = {
        'client_id': client_id,
        'response_type': response_type,
        'redirect_uri': redirect_url,
        'scope': scope
    }

    url = f"{url}?{urllib.parse.urlencode(params)}"

    return url

def getAuthorizationToken(body):
    url = 'https://accounts.spotify.com/authorize/api/token'
    headers = {
        'Authorization': 'Basic ' + getEncodedClient(),
        'content-type': 'application/x-www-form-urlencoded'
    }

    res = requests.post(url=url,
                        data=body,
                        headers=headers
                        )
    
    if(res.status_code != 200):
        print('auth.py> Error! - Something went wrong getting Auth Token!')
        print("\n" + res.text)
        return
    else:
        resJson = res.json()
        return resJson['access_token']

def getEncodedClient():
    string = config['CLIENT_ID'] + ":" + config['CLIENT_SECRET']
    stringBytes = string.encode("ascii")
    b64Bytes = base64.b64encode(stringBytes)
    b64String = b64Bytes.decode("ascii")
    
    return b64String
# print(getToken())
# print(getToken('Client Credentials'))

# print(getEncodedClient())
