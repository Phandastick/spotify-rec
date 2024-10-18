from auth import getToken
import requests
import random

access_token = getToken()
# access_token = '1'

def main():
    body = initInfo()
    sendRequest(body)
    return

def initInfo():
    if(not access_token):
        print('newTestPlaylist.py> Access token not found!')
        exit()

    # print(getArtistsList())
    # print(getGenreList())

    body = {
        'artistList': getArtistsList(),
        'genreList': getGenreList()
    }
    return body

def getArtistsList():
    artistList = []
    with open('./data/artists.csv', "r") as f:
        for artist in (f.readline().split(',')):
            artistList.append(artist)
    
    resultList = random.sample(artistList, k=3)
    return ",".join(resultList)

def getGenreList():
    genresList = []
    with open('./data/genres.csv', "r") as f:
        for artist in (f.readline().split(',')):
            genresList.append(artist)
    
    resultList = random.sample(genresList, k=2)
    return ",".join(resultList)

def sendRequest(data):
    data = initInfo()
    
    print(data['artistList'])
    print(data['genreList'])
    
    payload = {
        'limit': 50,
        'market': 'MY',
        'seed_artists': data['artistList'],
        'seed_genres': data['genreList']
    }

    url = 'https://api.spotify.com/v1/recommendations'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = requests.get(url=url,
                       params=payload,
                       headers=headers)
    
    print(res.text)

# print(getArtistsList())

# initInfo()
# print('Token: ', getToken())

main()