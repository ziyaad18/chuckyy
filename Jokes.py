import requests
from flask import Flask,render_template,url_for,redirect
w
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Random joke from chuck norris: </strong>" + response['value']


@app.route('/', methods=['GET'])
def get_chuck():

    url = 	"https://api.chucknorris.io/jokes/pfCp9FgBSO-eSZYhYW_k5w"
    response = requests.get(url).json()

    return "<strong>Random joke from chuck norris: </strong>" + response['value']




if __name__== "__main__":
    app.run(debug=True)
