-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS eddify_dev_db;
USE eddify_dev_db;
CREATE TABLE IF NOT EXISTS users ( 
    id INT NOT NULL AUTO_INCREMENT, 
    email VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    first_name VARCHAR(256) NOT NULL,
    last_name VARCHAR(256) NOT NULL,
    user_name VARCHAR(256) NOT NULL,
    image_file VARCHAR(256) NOT NULL,
    phone_number VARCHAR(256) NOT NULL,
    country  VARCHAR(256) NOT NULL,
    confirmed VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");
INSERT INTO users (email, password, first_name, last_name, user_name, image_file, phone_number, country, confirmed) VALUES ("shola@gmail.com", "12345", "shola", "ade", "sholacole", "//shola", "09022334555", "Nigeria", "no");

