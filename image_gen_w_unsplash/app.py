from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

#search images in Unsplash

def search_images(query):
    url = 'https://api.unsplash.com/search/photos'
    headers = {
        'Accept-Version': 'v1',
        'Authorization': 'Client-ID lqoNHCej6px126TP6IhWPj3_Oc3tIibBxkWevs9FccQ'
    }
    params = {
        'query': query,
        'per_page': 10, #number of images returned per page
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['results']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def search():
    query = request.form['query']
    images = search_images(query)
    return render_template('index.html',images=images)

if __name__ == '__main__':
    app.run(debug=True)