CREATE TABLE IF NOT EXISTS Clients(
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_username TEXT,
    client_password TEXT,
    client_balance REAL DEFAULT 0,
    client_message TEXT,
    client_email TEXT
);

CREATE TABLE IF NOT EXISTS Blocked_Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blocked_client_id INTEGER,
    blocked_client_date DATE,
    FOREIGN KEY (blocked_client_id) REFERENCES Clients(client_id)
);
