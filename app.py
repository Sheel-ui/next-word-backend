from flask import Flask
from flask_restful import Api
from src.api import NextWord
from dotenv import load_dotenv
from flask_cors import CORS

import os

app = Flask(__name__)
api = Api(app)
CORS(app)
load_dotenv()

api.add_resource(NextWord, os.getenv('ENDPOINT'))

if __name__ == '__main__':
    app.run(port=os.getenv('PORT'),host=os.getenv('HOST'),debug=True)