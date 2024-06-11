#!/usr/bin/python3
"""
We create a flask app with app_views
"""
from flask import jsonify
from api.v1.views import app_views


@app_viws.route('/status')
def api_status():
    ===

    ===

response = {'status': "OK"}
return jsonify(response)

