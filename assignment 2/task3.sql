CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,  
    name VARCHAR(255) NOT NULL,  
    email VARCHAR(255) UNIQUE NOT NULL  
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,  
    user_id INT NOT NULL,  
    amount DECIMAL(10, 2) NOT NULL,  
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    FOREIGN KEY (user_id) REFERENCES users(user_id)  
);
INSERT INTO users (name, email) VALUES 
('Alice Johnson', 'alice.johnson@example.com'),
('Bob Smith', 'bob.smith@example.com'),
('Charlie Brown', 'charlie.brown@example.com'),
('David Green', 'david.green@example.com'),
('Eva White', 'eva.white@example.com');

INSERT INTO orders (user_id, amount, order_date) VALUES 
(1, 120.50, '2023-01-01'),
(1, 45.30, '2023-01-15'),
(2, 200.00, '2023-01-10'),
(3, 75.00, '2023-02-01'),
(3, 60.50, '2023-02-10'),
(4, 300.00, '2023-01-05'),
(5, 50.00, '2023-02-03'),
(2, 100.00, '2023-01-20'),
(1, 200.00, '2023-02-05'),
(5, 80.00, '2023-03-01');

SELECT u.name, SUM(o.amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name
ORDER BY total_spent DESC;
