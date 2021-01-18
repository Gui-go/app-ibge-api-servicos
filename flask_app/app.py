from flask import Flask, jsonify
from flask_restful import Resource, Api
import json

from fct.get_regions import get_regions
from fct.get_namestat import get_namestat

app = Flask(__name__)

@app.route('/')
def get():
    return 'hell'

@app.route('/get/regions/<uf>') # Route to get a json with mun, micro, meso
def req_regions(uf):
    try:
        return get_regions(uf).to_json()
    except:
        return jsonify({'Error': 'Something wrong with the api call'})

@app.route('/get/meso/<uf>') # Route to get the meso names
def req_meso(uf):
    try:
        return jsonify(list(get_regions(uf)['nm_meso'].unique()))
    except:
        return jsonify({'Error': 'Something wrong with the api call'})

@app.route('/get/micro/<uf>') # Route to get the micro names
def req_micro(uf):
    try:
        return jsonify(list(get_regions(uf)['nm_micro'].unique()))
    except:
        return jsonify({'Error': 'Something wrong with the api call'})
    

@app.route('/get/mun/<uf>') # Route to get the mun names
def req_mun(uf):
    try:
        return jsonify(list(get_regions(uf)['nm_mun'].unique()))
    except:
        return jsonify({'Error': 'Something wrong with the api call'})


@app.route('/namestat/<nome>') # Route to get the name stats
def req_namestat(nome):
    try:
        return jsonify(get_namestat(nome))
    except:
        return jsonify({'Error': 'Something wrong with the api call'})


if __name__ == '__main__':
    app.run(debug=True, port=5000, host = "0.0.0.0")
