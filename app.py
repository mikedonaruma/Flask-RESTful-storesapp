from datetime import timedelta
from flask_restful import Api
from flask import Flask
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
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
