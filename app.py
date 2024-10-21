from flask import Flask, render_template,redirect
import requests
import newTestPlaylist as spotifyHelper

app = Flask(__name__)
app.config.update(
    SERVER_NAME = "http://localhost:5000"
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

    callbackurl = spotifyHelper.getToken(f'Authorization Code, {scope}')

    return redirect(callbackurl)

@app.route('/callback')
def callback(): 
    
    global token
    token = requests.get()

    #if success
    return redirect('/home')

@app.route('/home')
def home():
    print("app.py> Login Successful!")
    return render_template('index.html')


@app.route("/doUpdatePlaylist")
def updatePlaylist():
    print('app.py> Calling update playlist')

    #get artists and genres
    seed =  spotifyHelper.getSeeds()
    recTracks = spotifyHelper.getRecs(seed, access_token)
    spotifyHelper.updatePlaylist(recTracks)


# app.config('./config.cfg')