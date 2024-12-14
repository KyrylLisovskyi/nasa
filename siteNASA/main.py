import flask
import random
import requests
import config

r = random
f = flask
app = flask.Flask(__name__)
app.config.from_object(config.Config)

API = 'NHI4NGsNZnXCeVuNc38A27sZQzxPKx5WrVvfgfmq'

@app.route("/")
def nasa():
    url = f'https://api.nasa.gov/planetary/apod?api_key={API}'
    response = requests.get(url)
    data = response.json()
    return f.render_template("nasa.html", title="NASA", data=data)

app.run(port=10000, debug=True)