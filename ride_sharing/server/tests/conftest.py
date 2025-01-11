import pytest
from flask import Flask
from src.app.routes import initialise_routes


@pytest.fixture
def app():
    app = Flask(__name__)
    initialise_routes(app=app)
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client_app(app):
    return app.test_client()
