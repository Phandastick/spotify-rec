from flask import Flask, request

app = Flask(__name__)

@app.route('/dostuff')
def dostuff():
    print("Doing stuff")
    print(request.args.get('params'))

import auth
print(auth.getEncodedClient())