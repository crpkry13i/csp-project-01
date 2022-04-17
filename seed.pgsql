DROP DATABASE IF EXISTS users_db;
CREATE DATABASE users_db;

\c users_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'password');