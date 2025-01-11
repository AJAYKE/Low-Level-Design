from math import sqrt

from src.database.databaseObject import DatabaseObject
from src.utils.constants import UserRole, VehicleType


class Ride:
    def __init__(self, rider_id, type, source_location, destination_location):
        self.rider_id = rider_id
        self.vehicle_type: VehicleType = type
        self.source_location: list[float] = source_location
        self.destination_location: list[float] = destination_location
        self.fare = self.__fare_calculator()
        self.driver_id = self.__assign_driver()
        self.__db = DatabaseObject()

    def __fare_calculator(self):
        minimum_booking_fare = 10
        distance = self.__calculate_source_to_destination_distance()
        total_fare = minimum_booking_fare
        if self.vehicle_type == VehicleType.CAR.value:
            total_fare += distance * 4
        elif self.vehicle_type == VehicleType.AUTO.value:
            total_fare += distance * 3
        elif self.vehicle_type == VehicleType.BIKE.value:
            total_fare += distance * 2
        else:
            raise Exception(f"unknow vehicle type {self.vehicle_type}")
        return total_fare

    def __calculate_source_to_destination_distance(self):
        distance = sqrt(
            (self.source_location[0] - self.destination_location[0]) ** 2
            + (self.source_location[1] - self.destination_location[1]) ** 2
        )
        return distance

    def __assign_driver(self):
        query = f"""select top 1 id from users where user_role={UserRole.DRIVER.value} and is_active=1"""
        driver_id = self.__db.fetch_all(query=query, params=())
        return driver_id[0]  # database returns a tuple, so we are taking first value
