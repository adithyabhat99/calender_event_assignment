from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from database import init_db

app = Flask(__name__)
CORS(app)
init_db()

# wrapper used to authenticate routes
from auth import *
# routes
from user import *
from event import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
