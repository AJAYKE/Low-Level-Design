from enum import Enum


class BookFormat(str, Enum):
    HARDCOVER = "hardcover"
    PAPERBACK = "paperback"
    EBOOK = "ebook"
    AUDIOBOOK = "audiobook"
    MAGAZINE = "magazine"
    NEWSPAPER = "newspaper"


class BookStatus(str, Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"
    RESERVED = "reserved"
    LOST = "lost"


class AccountStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    BANNED = "banned"


class ReservationStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class Constants:
    MAX_BORROW_LIMIT = 5
    MAX_RESERVE_LIMIT = 3
    MAX_BORROW_DAYS = 14
    MAX_RESERVE_DAYS = 14
    LATE_FEE_PER_DAY = 10
