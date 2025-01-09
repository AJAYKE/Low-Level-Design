CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY;
    user_name varchar(16) not null;
    phoneNumber INT not null;
    country varchar(50) not null;
    email_id varchar(40) null;
    is_active boolean DEFAULT 1;
    user_role INT DEFAULT 1;
    COUNTRY and phoneNumber is unique
)