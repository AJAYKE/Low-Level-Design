from flask import Blueprint, jsonify, request
from src.services.ride_service import RideService
from src.services.user_service import UserService
from src.utils.validators import validate_location, validate_request_body

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


@user_routes.route("/users/<int:user_id>/update_to_driver", methods=["POST"])
def update_to_driver(user_id):
    response = user_service.update_to_driver(user_id=user_id)
    return jsonify(response), 201


ride_routes = Blueprint("ride_routes", __name__)
ride_service = RideService()


@ride_routes.route("/ride/create_ride", methods=["POST"])
def create_ride():
    data = request.get_json()
    if not (
        validate_request_body(
            data, ("user_id", "source_location", "destination_location")
        )
        and validate_location(data["source_location"])
        and validate_location(data["destination_location"])
    ):
        return jsonify({"error": "Invalid Request Body"}), 400

    response = ride_service.create_ride(data)
    return jsonify(response), 201


@ride_routes.route("/ride/<int:ride_id>/update_ride_start", methods=["POST"])
def update_ride_start(ride_id):
    response = ride_service.update_ride_start_time(ride_id)
    return jsonify(response), 201


@ride_routes.route("/ride/<int:ride_id>/ride_end", methods=["POST"])
def update_ride_end(ride_id):
    response = ride_service.update_ride_end_time(ride_id)
    return jsonify(response), 201


@ride_routes.route("/ride/get_ride_history", methods=["GET"])
def get_ride_history():
    user_id = request.args.get("user_id")
    page_num = request.args.get("page_num", 1)

    response = ride_service.get_all_rides(user_id=user_id, page_num=page_num)
    return jsonify(response), 200


def initialise_routes(app):
    app.register_blueprint(user_routes, url_prefix="/api/v1")
    app.register_blueprint(ride_routes, url_prefix="/api/v1")
