import json
import os
from flask import Flask, jsonify, abort, render_template

from async_data import get_data_async
template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def home():
    return render_template('root.html')


@app.route('/data')
def get_data():
    try:
        results = get_data_async()
    except:
        abort(404)

    return jsonify(results)


@app.route('/test/<int:file_id>')
def get_test_data(file_id: int):
    with open(f'./static/json/test_{file_id}.json') as json_file:
        return json.dumps(json.load(json_file))

