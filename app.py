from flask import Flask, jsonify, render_template,redirect, request
import requests, auth
import newTestPlaylist as spotifyHelper

DOMAINURL = "http://127.0.0.1:5000"

app = Flask(__name__)
app.config.update(
    SERVER_NAME = DOMAINURL
)

token = ""

@app.route("/")
def landing():
    print("Starting app...")
    return render_template('index.html')

@app.route('/login')
def login():
    print('app.py> Trying to log in...')
    scope = 'playlist-modify-public playlist-modify-private'

    url = spotifyHelper.getToken(f'Authorization Code,{scope}')
    # print('URL:',url)

    return redirect(url)

@app.route('/callback')
def callback(): 
    print('app.py> Callback accepted')
    if('error' in request.args):
        print('app.py> Error found! - authentication failed')
        return jsonify({
            "error": request.args['error']
        })

    if('code' in request.args):
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': f'{DOMAINURL}/callback'
        }

        #use auth code to get token
        token = auth.getAuthorizationToken(req_body)
        print('app.py: token',token)
    #if success
        return redirect('/home')
    return('Failed to get token from callback')

@app.route('/home')
def home():
    print("app.py> Login Successful!")
    return redirect('/doUpdatePlaylist')

@app.route("/doUpdatePlaylist")
def updatePlaylist():
    print('app.py> Calling update playlist')

    #get artists and genres
    seed =  spotifyHelper.getSeeds()
    recTracks = spotifyHelper.getRecs(seed, token)
    spotifyHelper.updatePlaylist(recTracks)

    return('Updated Playlist with random songs!')


# app.config('./config.cfg')