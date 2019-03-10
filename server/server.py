import os, sys, logging
from flask import Flask, json, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)

def usage():
    print ("python3 server.py")
    exit(1)

class Main(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id", type = str, location = 'json')
        self.reqparse.add_argument("pw", type = str, location = 'json')

    def post(self):
        args = self.reqparse.parse_args()
        print ("ID: ", args["id"])
        print ("PW: ", args["pw"])
        return make_response(jsonify(id=args["id"], pw=args["pw"]), 200)

api.add_resource(Main, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=True)
