

CREATE TABLE IF NOT EXISTS Accounts (
    AccountID SERIAL PRIMARY KEY,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Balance DECIMAL(10, 2) CHECK (Balance >= 0),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID SERIAL PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID),
    CONSTRAINT unique_transaction_id UNIQUE (TransactionID)
);

INSERT INTO Accounts (Email, Balance) VALUES ('john.doe@example.com', 100.00);

INSERT INTO Accounts (Email, Balance) VALUES ('john.doe@example.com', -100.00);

INSERT INTO Transactions (AccountID, Amount) VALUES (1, 50.00);

INSERT INTO Transactions (TransactionID, AccountID, Amount) VALUES (1, 1, 50.00);

SELECT * from Accounts;
SELECT * from Transactions;