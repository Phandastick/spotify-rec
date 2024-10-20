from auth import getToken
import requests
import random
import json 

access_token = getToken('Authorization Code')
playlistLimit =50
playlistID = '467DXKl4bPoQ8rVfwm4kyl'
# access_token = '1'

def main():
    body = getSeeds()
    tracks = getRecs(body) # list of strings

    updatePlaylist(tracks)
    return

def getSeeds():
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


def getRecs(data):
    data = getSeeds()
    
    # print(data['artistList'])
    # print(data['genreList'])
    
    payload = {
        'limit': playlistLimit,
        'market': 'MY',
        'seed_artists': data['artistList'],
        'seed_genres': data['genreList']
    }

    url = 'https://api.spotify.com/v1/recommendations'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        # "Content-Type": "application/x-www-form-urlencoded"
    }

    res = requests.get(url=url,
                       params=payload,
                       headers=headers)
    
    resJson = json.loads(res.text)

    # print(resJson)

    # song is --> tracks --> ID
    tracks = resJson['tracks']
    list = getIDs(tracks)
    
    return list

def getIDs(tracks):
    # print(type(tracks))
    trackIDs = []
    for track in tracks:
        trackIDs.append(track['id'])
    
    return trackIDs


def updatePlaylist(tracks):
    # for i in tracks:
    #     print(i)
    url = f'https://api.spotify.com/v1/playlists/{playlistID}/tracks'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    payload = { 
        'uris': getStringID(tracks)
    }

    res = requests.put(
        url=url,
        headers=headers,
        data=payload
    )

    print(res.status_code)
    print('\n' + res.text)

def getStringID(array):
    return ",".join(array)


# print(getArtistsList())

# getSeeds()
# print('Token: ', getToken())

main()