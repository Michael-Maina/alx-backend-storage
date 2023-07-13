-- creates a table users with id, email and name
CREATE TABLE IF NOT EXISTS users (
       id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email varchar(255) UNIQUE NOT NULL,
       name varchar(255)
);
