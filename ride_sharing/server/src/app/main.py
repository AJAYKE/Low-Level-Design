from flask import Flask

from ride_sharing.server.src.app.routes import initialise_routes


def create_app():
    app = Flask(__name__)
    app.config("JSONIFY_PRETTYPRINT_REGULAR") = True
    
    initialise_routes(app=app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)