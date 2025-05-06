class Notify:
    """
    Notify class to handle notifications for various events in the library management system.
    """

    def __init__(self, user_id: int, book_id: int, message: str):
        self.user_id = user_id
        self.book_id = book_id
        self.message = message

    def send_notification(self) -> None:
        """
        Send notification to the user.
        """
        # Logic to send notification (e.g., email, SMS, etc.)
        print(f"Notification sent to User ID {self.user_id}: {self.message}")
