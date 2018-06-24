from flask import Flask
from flask_restful import Api
import callables

# Placeholder Route
route = '/api/v1/parse/'

app = Flask(__name__)
api = Api(app)
api.add_resource(callables.ASC, f'{route}text=<text>')

if __name__ == '__main__':
    app.run(debug=True)