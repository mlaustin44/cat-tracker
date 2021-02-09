DROP TABLE IF EXISTS readings;

CREATE TABLE readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    uuid TEXT,
    bname TEXT,
    btimestamp INTEGER,
    rssi INTEGER
);