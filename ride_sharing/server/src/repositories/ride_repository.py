from src.database.databaseObject import DatabaseObject


class RideRepository:
    def __init__(self, db):
        self.db: DatabaseObject = db

    def create_ride(
        self, rider_id, driver_id, source_location, destination_location, fare
    ):
        query = """insert into rides (user_id,driver_id,source_location,destination_location,fare)
        values (%s,%s,%s,%s,%s)"""
        params = (
            rider_id,
            driver_id,
            str(source_location),
            str(destination_location),
            fare,
        )
        ride_id = self.db.execute(query=query, params=params)
        return ride_id

    def update_ride(self, field, value, ride_id):
        query = f"""update table rides set {field}=%s where id=%s"""
        params = (value, ride_id)
        self.db.execute(query=query, params=params)
