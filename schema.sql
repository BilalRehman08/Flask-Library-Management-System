CREATE DATABASE IF NOT EXISTS library_management_sys;
USE library_management_sys;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(45) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    user_type ENUM("ADMIN", "CUSTOMER"),
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS book_category;
CREATE TABLE book_category (
	id INT UNSIGNED NOT NULL,
    name VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS book;
CREATE TABLE book (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    quantity INT UNSIGNED NOT NULL DEFAULT 0,
    status ENUM("AVAILABLE", "NOT AVAILABLE"),
    PRIMARY KEY (id),
    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES book_category(id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE book_borrow (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id INT UNSIGNED NOT NULL,
    book_id INT UNSIGNED NOT NULL,
    status ENUM("ACCEPT", "REJECT", "PENDING"),
    checked_by INT UNSIGNED  NULL,
    checked_time DATETIME NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    CONSTRAINT fk_borrow_user_id FOREIGN KEY (user_id) REFERENCES user(id),
    CONSTRAINT fk_borrow_book_id FOREIGN KEY (book_id) REFERENCES book(id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;
