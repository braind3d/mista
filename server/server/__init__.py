'''
Embedded traffic light Flask server.

This module contains a Flask server containing handlers for the following paths:
    - GET /store/live
        Returns a stream from a .jpg generator using the Raspberry camera.

    - GET /store/status
        Returns the current status of the traffic light.

    - POST /traffic-light/animation
        Stores a new submitted animation json file.

    - POST /traffic-light/change_lights
        Sets the traffic lights to display certain passed animations.

Module tree:
    .
    ├── store
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   └── views.cpython-36.pyc
    │   └── views.py
    ├── __init__.py
    ├── models
    │   ├── camera.py
    │   ├── __init__.py
    │   ├── light_controller.py
    │   └── __pycache__
    │       ├── camera.cpython-36.pyc
    │       ├── __init__.cpython-36.pyc
    │       └── light_controller.cpython-36.pyc
    ├── __pycache__
    │   └── __init__.cpython-36.pyc
    ├── static
    │   └── animations
    │       ├── 3sec.json
    │       ├── empty.json
    │       └── filled.json
    ├── templates
    └── traffic_light
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-36.pyc
        │   └── views.cpython-36.pyc
        └── views.py

Usage:
    from server import create_app
    app = create_app()
    app.run(host='0.0.0.0', debug=True)

'''

from flask import Flask

from server.store.views import store_blueprint


def create_app(
        name: str = __name__,
        config: str = 'flask.cfg'
):
    '''
    Initializes the Flask server.

    Parameters:
    -----------
    name : str (default: __name__)
        Name of the server.

    config : str (default: 'flask.cfg')
        Configuration to be loaded.

    Returns:
    --------
    A Flask server app.
    '''

    app = Flask(
        name,
        template_folder='static/templates',
        instance_relative_config=True
    )

    app.config.from_pyfile(config)

    app.register_blueprint(store_blueprint)

    return app
