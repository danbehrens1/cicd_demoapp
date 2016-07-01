from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        text = "Hello World!"
        return text

class HelloClass(Resource):
    def get(self):
        text = "Hello Class!"
        return text

class HelloTest(Resource):
    def get(self):
        text = "Hello Test!"
        return text


api.add_resource(HelloWorld, '/hello/world')
api.add_resource(HelloClass, '/hello/class')
api.add_resource(HelloTest, '/hello/test')

if __name__ == '__main__':
    # Runn Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
    # pass
