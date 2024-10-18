from auth import getToken
import requests
import random

# access_token = getToken()
access_token = '1'

def initInfo():
    if(not access_token):
        print('newTestPlaylist.py> Access token not found!')
        exit()

    print(getArtistsList())
    print(getGenreList())

    queryData = {
        'artistList': getArtistsList(),
        'genreList': getGenreList()
    }

    return queryData

def getArtistsList():
    artistList = []
    with open('./data/artists.csv', "r") as f:
        for artist in (f.readline().split(',')):
            artistList.append(artist)
    
    resultList = random.sample(artistList, k=5)
    return ",".join(resultList)

def getGenreList():
    genresList = []
    with open('./data/genres.csv', "r") as f:
        for artist in (f.readline().split(',')):
            genresList.append(artist)
    
    resultList = random.sample(genresList, k=5)
    return ",".join(resultList)

def sendRequest(seed_artists):
    data = initInfo()
    seed_artists = artistsList
    seed_genres = genreList

    settings = {
        'limit': 50,
        'market': 'MY',
        'seed_artists': seed_artists,
        'seed_genres': seed_genres
    }

    url = 'https://api.spotify.com/v1/recommendations'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    body = {
        'limit': settings['limit'],
        'market': settings['market']
    }

# print(getArtistsList())

# initInfo()