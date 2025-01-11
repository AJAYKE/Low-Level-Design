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
