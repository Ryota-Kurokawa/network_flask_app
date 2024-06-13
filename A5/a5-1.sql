.open a5-1.db
.mode box
DROP TABLE IF EXISTS events;
CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, place TEXT);
INSERT INTO events(name, date, place) VALUES('りんごfes1','2020-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes2','2021-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes3','2022-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes4','2023-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes5','2024-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes6','2025-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes7','2026-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes8','2027-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes9','2028-10-04','青森');
INSERT INTO events(name, date, place) VALUES('りんごfes10','2029-10-04','青森');
SELECT * FROM events;
SELECT * FROM events WHERE name = 'りんごfes5';
SELECT * FROM events WHERE date > '2024-05-06';
SELECT * FROM events WHERE date < '2024-05-06' AND name = 'りんごfes9';