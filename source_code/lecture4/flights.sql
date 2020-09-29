-- Create flights table
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

-- Inserts
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);
INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);

-- Selects
SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = "New York";
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
SELECT * FROM flights WHERE duration > 500 OR destination = "Paris";
SELECT * FROM flights WHERE origin IN ("New York", "Lima");
SELECT * FROM flights WHERE origin LIKE "%a%";

-- Update
UPDATE flights SET duration = 430 WHERE origin = "New York" AND destination = "London";

-- Delete
DELETE FROM flights WHERE destination = "Tokyo";

-- Join
SELECT first, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id;

