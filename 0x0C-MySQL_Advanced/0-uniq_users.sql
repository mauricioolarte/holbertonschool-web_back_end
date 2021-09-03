-- SQL script that creates a table users
-- attributes id, email, name
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);