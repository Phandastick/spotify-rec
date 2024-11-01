# https://developer.spotify.com/dashboard/53ae987f426c4b45abc75b761d0bd49c/settings

import requests
import base64
from dotenv import dotenv_values
import urllib
DOMAINURL = "127.0.0.1:5000"

config = dotenv_values()

# print(config)

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

        return resJson
    else:
        print('auth.py> Request for access token failed!')
        print(res)
        return('auth.py> Error in getting Client Credentials!')
    
def getAuthorizationCode(scope):
    print('auth.py> Getting auth code...')
    url = 'https://accounts.spotify.com/authorize'
    client_id = config['CLIENT_ID']
    response_type = 'code'

    params = {
        'client_id': client_id,
        'response_type': response_type,
        'redirect_uri': f'http://{DOMAINURL}/callback',
        'scope': scope #dynamic argument
    }

    #returns spotify page url for spotify login
    url = f"{url}?{urllib.parse.urlencode(params)}"

    return url

def getAuthorizationToken(body):
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + getEncodedClient(),
        'content-type': 'application/x-www-form-urlencoded'
    }

    res = requests.post(
        url=url,
        data=body,
        headers=headers
    )
    
    if(res.status_code != 200):
        print('auth.py> Error! - Something went wrong getting Auth Token!')
        print(res.text)
        return res
    else:
        return res.json()

def getEncodedClient():
    string = config['CLIENT_ID'] + ":" + config['CLIENT_SECRET']
    stringBytes = string.encode("ascii")
    b64Bytes = base64.b64encode(stringBytes)
    b64String = b64Bytes.decode("ascii")
    
    return b64String
# print(getToken())
# print(getToken('Client Credentials'))

# print(getEncodedClient())
