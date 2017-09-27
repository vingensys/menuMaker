# Import flask dependencies
from flask import Blueprint, request, jsonify, make_response, abort#, render_template,flash, g, session, redirect, url_for

# Import the database object from the database model module
#from menuMaker.model import Category, Item, Invoice, ItemList

# Import the database connectivity session and declarative base from the app root 
from MenuMaker import Base, session

# Import module API
from MenuMaker.modAPI.menu import Menu

# Define the blueprint: 'api', set its url prefix: app.url/api
modAPI = Blueprint('api', __name__, url_prefix='/api')

# Set the route and accepted methods
@modAPI.route('/menu/', methods=['GET'])
def getMenu():
    # Initiate a Menu obj
    menuObj = Menu(session)
    menu = menuObj.getMenuList()
    return make_response(jsonify(menu))

@modAPI.route('/menu/<int:menu_id>', methods=['GET'])
def getMenuItem(menu_id):
    # Initiate a Menu obj
    menuObj = Menu(session)
    menuItem = menuObj.getMenuItem(menu_id)
    if 'respCode' in menuItem :
        if (menuItem['respCode'] == 404):
            abort(404)
    return make_response(jsonify(menuItem))        

@modAPI.route('/category/', methods=['GET'])
def getCat():
    # Initiate a Menu obj
    menuObj = Menu(session)
    category = menuObj.getCategoryList()
    return make_response(jsonify(category))

@modAPI.route('/category/<int:cat_id>', methods=['GET'])
def getCatItem(cat_id):
    # Initiate a Menu obj
    menuObj = Menu(session)
    catItem = menuObj.getCatItem(cat_id)
    if 'respCode' in catItem :
        if (catItem['respCode'] == 404):
            abort(404)
    return make_response(jsonify(catItem))        
