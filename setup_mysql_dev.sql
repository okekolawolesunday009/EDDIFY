-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS eddify_dev_db;

-- Create of upade the user 'eddify_dev' with the specified password
CREATE USER IF NOT EXISTS 'eddify_dev'@'localhost' IDENTIFIED BY 'eddify_dev_pwd';

-- Grant all priviledges on 'eddify_dev_db' to 'eddify_dev'
GRANT ALL PRIVILEGES ON eddify_dev_db.* TO 'eddify_dev'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'eddify_dev'@'localhost';
-- Flush privilegees to apply changes
FLUSH PRIVILEGES;
