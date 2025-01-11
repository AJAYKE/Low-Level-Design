from datetime import datetime

from src.database.databaseObject import DatabaseObject
from src.models.ride import Ride
from src.repositories.ride_repository import RideRepository
from src.utils.constants import PAGE_LIMIT


class RideService:
    def __init__(self):
        self.db = DatabaseObject()
        self.ride_repository = RideRepository()

    def create_ride(self, data):
        ride = Ride(
            rider_id=data["user_id"],
            source_location=data["source_location"],
            destination_location=data["destination_location"],
        )
        ride_id = self.ride_repository.create_ride(
            rider_id=ride.rider_id,
            driver_id=ride.driver_id,
            source_location=ride.source_location,
            fare=ride.fare,
            destination_location=ride.destination_location,
        )
        return {
            "data": {"ride_id": ride_id},
            "message": "Your Ride is successfully booked, your ride is on the way",
        }

    def update_ride_start_time(self, ride_id):
        self.ride_repository.update_ride("ride_start_time", datetime.now(), ride_id)
        return {"message": "ride started"}

    def update_ride_end_time(self, ride_id):
        self.ride_repository.update_ride("ride_end_time", datetime.now(), ride_id)
        return {"message": "ride ended"}

    def get_all_rides(self, user_id, page_num=1):
        range_start = PAGE_LIMIT * (page_num - 1)
        range_end = PAGE_LIMIT * page_num

        query = f"select ride_id, source_location, destination_location, fare, users.user_name from rides join users on rides.driver_id = users.id where user_id=%s LIMIT {range_end} OFFSET {range_start}"

        params = user_id

        ride_history = self.db.fetch_all(query=query, params=params)

        return {
            "data": {
                "format": [
                    "ride_id",
                    "source_location",
                    "destination_location",
                    "fare",
                    "driver_name",
                ],
                "rides": ride_history,
            },
            "message": "ride history fetched successfully",
        }
