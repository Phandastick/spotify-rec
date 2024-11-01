import requests, random, json 

playlistLimit = 50
playlistID = '467DXKl4bPoQ8rVfwm4kyl'


def main():
    body = getSeeds()
    tracks = getRecs(body) # list of strings

    updatePlaylist(tracks)
    return

def getSeeds():
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

def getRecs(seeds, access_token):

    # print('Calling getRecs with token:',access_token)
    
    # print(data['artistList'])
    # print(data['genreList'])
    
    payload = {
        'limit': playlistLimit,
        'market': 'MY',
        'seed_artists': seeds['artistList'],
        'seed_genres': seeds['genreList']
    }

    url = 'https://api.spotify.com/v1/recommendations'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        # "Content-Type": "application/x-www-form-urlencoded"
    }

    res = requests.get(url=url,
                       params=payload,
                       headers=headers)
    
    if(res.status_code != 200):
        print("newTestPlaylist.py> Something went wrong with recommendations!")
        return
    resJson = json.loads(res.text)
    # print(resJson)

    # song is --> tracks --> ID
    logTracks(resJson)
    tracks = resJson['tracks']
    list = getIDs(tracks)
    
    return list

def getIDs(tracks):
    # print(type(tracks))
    trackIDs = []
    for track in tracks:
        trackIDs.append(track['id'])
    
    return trackIDs

def logTracks(tracks):
    string = json.dumps(tracks)
    with open('log.json',"w") as f:
        f.write(string)

def updatePlaylist(tracks, access_token):

    print('''-----------------Updating Playlist----------------------
            \n Tracks:''')
    
    for i in tracks:
        print(i)

    print('----------------------------------------------------------------------')

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
        params=payload
    )
    
    if (res.status_code != 200):
        print('newTestPlaylist.py> Update went wrong!')
        print(res.text)
    else:
        print('\nUpdated Playlist successfully!')
        print('\nUpdated Playlist: ' + res.text)

def getStringID(array):
    newArray = []

    for i in array:
        newArray.append('spotify:track:'+i)

    return ",".join(newArray)


# print(getArtistsList())

# getSeeds()

# main()1