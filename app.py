import os
import re

from db import db
from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# workaround for SQLAlchemy no longer working with Heroku Postgres
uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db') # get will use sqlite if it cant find databaseurl in heroku
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # config JWT to expire within half an hour
app.secret_key = 'jose' # this needs to be secret, and it should be secure, aka long and complicated
api = Api(app)

# JWT() creates a new endpoint, /auth, when we call /auth, we send it a username and a password, JWT gets the username and pass and sends it to the JWT function
# if the user is autherized, the /auth endpoint will return a JW token.

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
