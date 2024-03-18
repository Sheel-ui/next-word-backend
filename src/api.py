from flask import request
from flask_restful import Resource
from src.predict import Predictor
import json

nextWord = Predictor()

class NextWord(Resource):

    def get(self):
        return {
            "status": "success",
            "message": "Service is running"
            }

    def post(self):
        try:
            data = json.loads(request.data)
            text = data['text']
            predictions = int(data['predictions'])
            tokens = int(data['tokens'])
            result = nextWord.gen_m_words_n_predictions(tokens,predictions,text)
            return {
                'status':"success",
                'words': result
            }
        except Exception as e:
            return { "error": "Something went wrong: {} {}".format(type(e).__name__,e) }