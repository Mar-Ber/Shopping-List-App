from __future__ import annotations

from flask import Flask
from flask_restful import Api, reqparse

from resources import *

app = Flask(__name__)
api = Api(app)
api.add_resource(resource=ItemManagerAPI, urls="/manage",endpoint = "bar")

if __name__ == '__main__':
    app.run(debug=True)