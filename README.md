# Replace new recommendations to spotify playlist

Look, I get bored of the same 50 songs somehow in the discover weekly playlist by Spotify...

So I made a thing
[Playlist Link](https://open.spotify.com/playlist/467DXKl4bPoQ8rVfwm4kyl)

## New dailies

Using a new playlist, running this script should allow you to update your playlist with new songs given a limit of songs, replacing the old songs completely.

## Installation

Using Venv

```
py -3 -m venv .venv
.venv/Scripts/activate //make sure you have permission to run scripts

pip install requirements.txt
```

Using pipenv
```
pipenv shell
pipenv install requirements.txt
```

### Setting up env
1. create .env
2. get CLIENT_ID and CLIENT_SECRET
3. Generate SECRET_KEY with
```
import os
os.urandom(24)
```

## Running
Use flask to start 'webapp' and run the api

```
flask run
flask run --debug
```

1. Probably change playlist ID to yours in playlist.py
2. Site should be running on 127.0.0.1
3. Click on **login** button in order to use the /login route
4. ¯\\_(ツ)_/¯
5. yay