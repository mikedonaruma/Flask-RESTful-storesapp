# Stores REST API

This is built with Flask, Flask-RESTful, Flask-JWT and Flask-SQLAlchemy.
SQLite DB when run locally, Postgres DB when run through Heroku.

Deployed on Heroku.

## Endpoints:
```
GET   /items - a list of all items
GET   /item/<name> - details on an item
POST  /item/<name> - add a new item. price, store_id are required
PUT   /item/<name> - update/create new item. 
DEL   /item/<name> - remove an item.

GET   /stores - a list of all stores.
GET   /store/<name> - details of a store.
POST  /store/<name> - add a new store. 
DEL   /store/<name> - remove a store.

POST  /auth - authenticate
POST  /register - register a new user. username, password are required
```
