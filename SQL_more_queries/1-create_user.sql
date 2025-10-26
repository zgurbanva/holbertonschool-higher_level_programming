-- CREATE user_0d_1 WITH FULL PRIVILEGES
-- Creates user 'user_0d_1'@'localhost' with password and grants all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant full privileges on the server (all databases/tables)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
