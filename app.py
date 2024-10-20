from flask import Flask
import newTestPlaylist as spotifyHelper

app = Flask(__name__)

@app.route("/")
def landing():
    print("Starting app...")

@app.route("/doUpdatePlaylist")
def updatePlaylist():
    #get artists and genres
    seed =  spotifyHelper.getSeeds()
    recTracks = spotifyHelper.getRecs(seed)
    spotifyHelper.updatePlaylist(recTracks)