from abc import ABC

from ride_sharing.server.src.utils.constants import VehicleType


class Vehicle(ABC):
    def __init__(self):
        self.vehilce_type: VehicleType = None
        self.vehicle_number: str = None
