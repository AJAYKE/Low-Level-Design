CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(16) NOT NULL,
    phone_number BIGINT NOT NULL,
    country VARCHAR(50) NOT NULL,
    email_id VARCHAR(40),
    is_active BOOLEAN DEFAULT TRUE,
    user_role INT DEFAULT 1,
    UNIQUE (country, phone_number)
);


CREATE TABLE IF NOT EXISTS RIDES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    driver_id INT NOT NULL,
    source VARCHAR(30) NOT NULL,
    destination VARCHAR(30) NOT NULL,
    fare INT NOT NULL,
    ride_booking_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    ride_start_time DATETIME DEFAULT NULL,
    ride_end_time DATETIME DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (driver_id) REFERENCES users(id)
);