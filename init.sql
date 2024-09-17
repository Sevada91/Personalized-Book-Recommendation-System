CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    authors TEXT,
    category VARCHAR(255),
    publish_date VARCHAR(50)
);