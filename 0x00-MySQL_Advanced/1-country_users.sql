-- creates a table users with id, email, name and country
CREATE TABLE IF NOT EXISTS users (
       id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email varchar(255) UNIQUE NOT NULL,
       name varchar(255),
       country varchar(2) NOT NULL DEFAULT 'US'
);
