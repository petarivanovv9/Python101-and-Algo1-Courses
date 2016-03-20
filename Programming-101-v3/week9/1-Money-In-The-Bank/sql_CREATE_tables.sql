CREATE TABLE IF NOT EXISTS Clients(
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_username TEXT NOT NULL UNIQUE,
    client_password TEXT,
    client_balance REAL DEFAULT 0,
    client_message TEXT,
    client_email TEXT
);

CREATE TABLE IF NOT EXISTS Blocked_Clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blocked_client_id INTEGER,
    blocked_client_date DATE,
    FOREIGN KEY (blocked_client_id) REFERENCES Clients(client_id)
);

CREATE TABLE IF NOT EXISTS Bank_Accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bank_acc_balance INTEGER,
    bank_acc_name TEXT,
    bank_acc_client_id INTEGER,
    FOREIGN KEY (bank_acc_client_id) REFERENCES Clients(client_id)
);

CREATE TABLE IF NOT EXISTS Clients_Tans(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    tan_code TEXT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);
