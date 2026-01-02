CREATE TABLE IF NOT EXISTS Authors (
    AuthorID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Bio TEXT
);

CREATE TABLE IF NOT EXISTS Categories (
    CategoryID SERIAL PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Books (
    BookID SERIAL PRIMARY KEY,
    ISBN VARCHAR(20) UNIQUE NOT NULL,
    Title VARCHAR(255) NOT NULL,
    AuthorID INT,
    CategoryID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

INSERT INTO Authors (Name, Bio) VALUES 
('J.K. Rowling', 'Author of the Harry Potter series'),
('George R. R. Martin', 'Author of A Song of Ice and Fire'),
('J.R.R. Tolkien', 'Author of The Lord of the Rings');

INSERT INTO Categories (CategoryName) VALUES
('Fantasy'),
('Adventure'),
('Mystery');

INSERT INTO Books (ISBN, Title, AuthorID, CategoryID) VALUES
('9780747532743', 'Harry Potter and the Philosopher\'s Stone', 1, 1),
('9780553103540', 'A Game of Thrones', 2, 2),
('9780261103573', 'The Hobbit', 3, 1);

SELECT b.Title AS BookTitle, a.Name AS AuthorName, c.CategoryName AS CategoryName
FROM Books b
JOIN Authors a ON b.AuthorID = a.AuthorID
JOIN Categories c ON b.CategoryID = c.CategoryID;
