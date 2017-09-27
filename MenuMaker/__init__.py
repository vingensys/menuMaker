from flask import Flask, make_response, jsonify
from json import dumps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from MenuMaker.model import Base, Category, Item, Invoice, ItemList

# Create Engine for DB connection
engine = create_engine('sqlite:///MenuMaker/menuMaker.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the database session object
# session instantiates a DBSession
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Define the WSGI application object
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def not_found(error):
        return make_response(jsonify({'error': 'Server Error'}), 404)
        
@app.route('/')
@app.route('/index/')
def index():
    return make_response(jsonify({'info': '(c) Menu Maker REST API'}))

# Import a module / component using its blueprint handler variable (modAPI)
from MenuMaker.modAPI.controllers import modAPI as api

# Register blueprint(s)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
