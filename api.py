from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from helpers import *

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()
parser.add_argument("sentence", type=str, help="sentence or words should be unicode text", location='form')
parser.add_argument("text", type=str, help="text should be unicode text", location='form')


class Spell(Resource):
    def get(self):
        return {"message": "Welcome to SpellAPI.", "status": 200}

    def post(self):
        args = parser.parse_args()

        text = args["sentence"]
        result = {}
        if text:
            suggestions = sym_spell.lookup_compound(sym_spell.word_segmentation(text).corrected_string, max_edit_distance=2, transfer_casing=True)
            for suggestion in suggestions:
                result["corrected"] = suggestion.term
            return jsonify(result)
        else:
            return {"sentence parameter is missing": 404}


class Split(Resource):
    def get(self):
        return {"message": "Welcome to SpellAPI.", "status": 200}

    def post(self):
        args = parser.parse_args()

        text = args["text"]
        if text:
            doc = nlp(text)
            sentences = []
            for sent in doc.sents:
                sentences.append(sent.text.strip())
            return jsonify(sentences)
        else:
            return {"text parameter is missing": 404}


api.add_resource(Spell, "/spell")
api.add_resource(Split, "/split")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
