from datetime import datetime, timedelta


class DateTimeUtils:
    @staticmethod
    def today():

        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def due_date(days: int) -> str:
        due_date = datetime.now() + timedelta(days=days)
        return due_date.strftime("%Y-%m-%d")
