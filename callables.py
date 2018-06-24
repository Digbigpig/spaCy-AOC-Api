from flask_restful import Resource
from flask import jsonify
import process


class ASC(Resource):
    def get(self, text):
        result = {'data': process.asc_parser(text)}
        return jsonify(result)
