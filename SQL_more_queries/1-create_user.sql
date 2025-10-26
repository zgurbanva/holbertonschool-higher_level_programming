-- CREATE user_0d_1 WITH FULL PRIVILEGES
-- Creates 'user_0d_1'@'localhost' with password and grants all privileges server-wide
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
