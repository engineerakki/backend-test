from flask import Flask
from datetime import timedelta
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jdasdaas2342as23qq'
app.config['JWT_TOKEN_LOCATION'] = ['query_string']
app.config['JWT_QUERY_STRING_NAME'] = 'sessionkey'

jwt = JWTManager(app)

import src.controllers