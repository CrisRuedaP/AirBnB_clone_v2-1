#!/usr/bin/python3
"""
app file for the api
"""

from os import getenv
from flask import Flask, jsonify
from flask import Blueprint
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.teardown_appcontext
def teardown_appcontext(self):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Returns a JSON-formatted 404 status code response"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    """Docstring"""
    HBNB_API_HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    HBNB_API_PORT = getenv('HBNB_API_PORT', '5000')
    app.run(host=HBNB_API_HOST,
            port=HBNB_API_PORT,
            threaded=True, debug=True)
