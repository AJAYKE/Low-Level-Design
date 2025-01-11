from flask import Blueprint, jsonify, request
from src.services.user_service import UserService
from src.utils.validators import validate_request_body

user_routes = Blueprint("user_routes", __name__)
user_service = UserService()


@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not validate_request_body(data, ["user_name", "country", "phone_number"]):
        return jsonify({"error": "Invalid Request Body"}), 400

    response = user_service.create_user(data)
    return jsonify(response), 201


@user_routes.route("/users/<int:user_id>/block", methods=["POST"])
def block_user(user_id):
    response = user_service.block_user(user_id=user_id)
    return jsonify(response), 201


def initialise_routes(app):
    app.register_blueprint(user_routes, url_prefix="/api/v1")
