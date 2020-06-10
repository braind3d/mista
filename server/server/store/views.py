'''
Blueprint of the '/store' server path.

This module contains a Flask server containing handlers for the following paths:
    - GET /live
        Returns a stream from a .jpg generator using the Raspberry camera.

    - GET /status
        Returns the current status of the traffic light.

Usage:
    from server.store.views import store_blueprint
    app.register_blueprint(store_blueprint)
'''

# Imports
from flask import Response, Blueprint, render_template, request
from server.database.controllers.games import Games

# Config
store_blueprint = Blueprint('store', __name__)


# Routes
@store_blueprint.route('/', methods=['GET'])
def index():
    '''
    GET /
    ---------
    Returns the homepage of the store.
    '''
    return render_template("index.html")


@store_blueprint.route('/gameslist', methods=['GET'])
def gameslist():
    '''
    GET /
    ---------
    Returns the homepage of the store.
    '''

    page_number = request.args.get("page", default=1, type=int)
    page_size = request.args.get("size", default=10, type=int)
    return render_template(
        "gameslist.html",
        games=Games.all(page_number, page_size, request.args.get('search_query')))


@store_blueprint.route('/app', methods=['GET'])
def app():
    '''
    GET /app
    -----------
    Returns the current status of the traffic light.
    '''
    return render_template('app.html', game=Games.get(int(request.args.get('id'))))