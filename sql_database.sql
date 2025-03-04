CREATE DATABASE library;
USE library;

CREATE TABLE staff (
    staff_ID INT NOT NULL AUTO_INCREMENT,
    staff_name CHAR(15) NOT NULL,
    staff_last_name CHAR(15) NOT NULL,
    staff_email CHAR(20) NOT NULL,
    staff_password CHAR(18) NOT NULL,
    PRIMARY KEY (staff_ID)
);

CREATE TABLE author (
    author_ID INT NOT NULL AUTO_INCREMENT,
    author_name CHAR(15) NOT NULL,
    author_last_name CHAR(15) NOT NULL,
    PRIMARY KEY (author_ID)
);

CREATE TABLE book (
    book_ID INT NOT NULL AUTO_INCREMENT,
    title CHAR(50) NOT NULL,
    author_ID INT NOT NULL,
    year INT,
    category CHAR(15),
    PRIMARY KEY (book_ID),
    FOREIGN KEY (author_ID) REFERENCES author(author_ID)
);

CREATE TABLE user (
    user_ID INT NOT NULL AUTO_INCREMENT,
    first_name CHAR(20) NOT NULL,
    last_name CHAR(20) NOT NULL,
    phone_number CHAR(15),
    email CHAR(35),
    registration_date DATE,
    membership_type CHAR(10),
    user_password CHAR(20),
    PRIMARY KEY (user_ID)
);

CREATE TABLE loan (
    loan_ID INT NOT NULL AUTO_INCREMENT,
    book_ID INT NOT NULL,
    user_ID INT NOT NULL,
    loan_date DATE,
    return_date DATE,
    PRIMARY KEY (loan_ID),
    FOREIGN KEY (book_ID) REFERENCES book(book_ID),
    FOREIGN KEY (user_ID) REFERENCES user(user_ID)
);