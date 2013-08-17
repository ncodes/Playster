# Server: Servers all pages displayed in the app view

from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def runServer():
    print 'Server started'

def start(playster):
    """ Starts the server in another thread """
    t = threading.Thread(target=runServer, args=())
    t.daemon = True
    t.start()