from app import auth
import datetime
from flask import Flask, jsonify, render_template,redirect, request, session
import app.playlist as spotifyAPI
from app.auth import DOMAINURL;

app = Flask(__name__)
app.config.update(
    SERVER_NAME = DOMAINURL
)

app.secret_key = auth.config['SECRET_KEY']
token = ""

# region spotify login
@app.route("/")
def landing():
    print("Starting app...")
    return render_template('index.html')

@app.route('/login')
def login():
    print('app.py> Trying to log in...')
    scope = 'playlist-modify-public playlist-modify-private'

    url = auth.getAuthorizationCode(scope)
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
            'redirect_uri': f'http://{DOMAINURL}/callback'
        }   

        #use auth code to get token
        tokeninfo = auth.getAuthorizationToken(req_body)

        if('access_token' in tokeninfo):
            # add session token info
            session['access_token'] = tokeninfo['access_token']
            session['refresh_token'] = tokeninfo['refresh_token']
            session['expires_at'] = datetime.datetime.now().timestamp() + tokeninfo['expires_in']

            # print('app.py> token',session['access_token'])
            return redirect('/home')
        else:
            return('app.py/callback> Something failed getting token info!')
    else:
        return('app.py> Failed to get token from callback')

# endregion

@app.route('/home')
def home():
    print("app.py> Login Successful!")
    return redirect('/doUpdatePlaylist')

#region spotify functions

@app.route("/doUpdatePlaylist")
def updatePlaylist():
    print('app.py> Calling update playlist')

    #get artists and genres
    seed =  spotifyAPI.getSeeds()
    recTracks = spotifyAPI.getRecs(seed, session['access_token'])
    spotifyAPI.updatePlaylist(recTracks, session['access_token'])

    return('Updated Playlist with random songs!')

#endregion

# region youtube search
# get all links from a given playlist
# youtube search api for each link
# put link in log file
@app.route('/doGetYTLinks')
def doGetYTLinks():
    print('app.py> doGetYTLinks Called')
    reqDict = request.args.to_dict
    



#endregion

# app.config('./config.cfg')