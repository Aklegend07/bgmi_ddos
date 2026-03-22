from flask import Flask
from threading import Thread
import logging

# Disable Flask's default logging to keep your terminal clean
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')

@app.route('/')
def home():
    return "Bot is running! 🚀"

def run():
    # Codespaces uses port 8080 by default for web traffic
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True # This ensures the server dies if the main bot dies
    t.start()
