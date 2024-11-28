DROP DATABASE IF EXISTS `AIRLINE`;
CREATE DATABASE IF NOT EXISTS AIRLINE;
USE AIRLINE;


-- Airport Table
CREATE TABLE IF NOT EXISTS Airport (
    Ap_name VARCHAR(100) PRIMARY KEY,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL
);

-- Airline Table
CREATE TABLE IF NOT EXISTS Airline (
    Airline_ID VARCHAR(100) PRIMARY KEY,
    Airline_name VARCHAR(100) UNIQUE NOT NULL
);

-- Flight_Employee Table
CREATE TABLE IF NOT EXISTS Flight_Employee (
    Emp_id VARCHAR(100) PRIMARY KEY,
    F_name VARCHAR(100) NOT NULL,
    M_name VARCHAR(100),
    L_name VARCHAR(100),
    Jobtype VARCHAR(50) NOT NULL,
    Salary FLOAT,
    Bdate DATE NOT NULL,
    Works_For VARCHAR(100),
    ManagerID VARCHAR(100),
    FOREIGN KEY (Works_For) REFERENCES Airline(Airline_ID),
    FOREIGN KEY (ManagerID) REFERENCES Flight_Employee(Emp_id)
);
-- Employee_Phone Table
CREATE TABLE IF NOT EXISTS Employee_Phone (
    Phone_No VARCHAR(15),
    PID VARCHAR(100),
    PRIMARY KEY (Phone_No, PID),
    FOREIGN KEY (PID) REFERENCES Flight_Employee(Emp_id)
);
-- Airplane Table
CREATE TABLE IF NOT EXISTS Airplane (
    AirplaneID VARCHAR(100) PRIMARY KEY,
    Aircraft_Model VARCHAR(100) NOT NULL,
    Flying_Hours FLOAT,
    SeatingCapacity INT NOT NULL
);

-- Flight Table
CREATE TABLE IF NOT EXISTS Flight (
    Flight_code VARCHAR(100) PRIMARY KEY,
    Source VARCHAR(100),
    Destination VARCHAR(100),
    AirplaneID VARCHAR(100) NOT NULL,
    Pilot VARCHAR(100) NOT NULL,
    Arrival TIMESTAMP NOT NULL,
    Departure TIMESTAMP NOT NULL,
    FOREIGN KEY (Source) REFERENCES Airport(Ap_name),
    FOREIGN KEY (Destination) REFERENCES Airport(Ap_name),
    FOREIGN KEY (AirplaneID) REFERENCES Airplane(AirplaneID),
    FOREIGN KEY (Pilot) REFERENCES Flight_Employee(Emp_id)
);

-- Passenger Table
CREATE TABLE IF NOT EXISTS Passenger (
    PID VARCHAR(100) PRIMARY KEY,
    F_name VARCHAR(100) NOT NULL,
    M_name VARCHAR(100),
    L_name VARCHAR(100),
    Bdate DATE NOT NULL,
    BoardingFlight VARCHAR(100) NOT NULL,
    FOREIGN KEY (BoardingFlight) REFERENCES Flight(Flight_code)
);
-- Employee_Phone Table
CREATE TABLE IF NOT EXISTS Passenger_Phone (
    Phone_No VARCHAR(15),
    PID VARCHAR(100),
    PRIMARY KEY (Phone_No, PID),
    FOREIGN KEY (PID) REFERENCES Passenger(PID)
);
-- First_Class_Passenger Table
CREATE TABLE IF NOT EXISTS First_Class_Passenger (
    PID VARCHAR(100) PRIMARY KEY,
    PrivateSuite BOOLEAN NOT NULL,
    SleepPodAvailability BOOLEAN NOT NULL,
    FOREIGN KEY (PID) REFERENCES Passenger(PID)
);
CREATE TABLE IF NOT EXISTS First_Class_Services (
    PID VARCHAR(100),
    FirstClassServices VARCHAR(100),
    PRIMARY KEY (PID, FirstClassServices),
    FOREIGN KEY (PID) REFERENCES  First_Class_Passenger(PID)
);


-- Business_Class_Passenger Table
CREATE TABLE IF NOT EXISTS Business_Class_Passenger (
    PID VARCHAR(100) PRIMARY KEY,
    BusinessLoungeAccess BOOLEAN NOT NULL,
    PriorityBoarding BOOLEAN NOT NULL,
    WorkstationAvailability BOOLEAN NOT NULL,
    FOREIGN KEY (PID) REFERENCES Passenger(PID)
);
CREATE TABLE IF NOT EXISTS Business_Class_Services (
    PID VARCHAR(100),
    BusinessClassServices VARCHAR(100),
    PRIMARY KEY (PID, BusinessClassServices),
    FOREIGN KEY (PID) REFERENCES Business_Class_Passenger(PID)
);

-- Dependents Table
CREATE TABLE IF NOT EXISTS Dependents (
    Name VARCHAR(100) NOT NULL,
    DOB DATE NOT NULL,
    Relationship VARCHAR(50),
    Depends_on VARCHAR(100),
    PRIMARY KEY (Relationship, Depends_on),
    FOREIGN KEY (Depends_on) REFERENCES Flight_Employee(Emp_id)
);

-- Baggage Table
CREATE TABLE IF NOT EXISTS Baggage (
    BaggageId CHAR(5) NOT NULL,
    Weight FLOAT NOT NULL,
    BelongsTo VARCHAR(100),
    PRIMARY KEY (BaggageId, BelongsTo),
    FOREIGN KEY (BelongsTo) REFERENCES Passenger(PID)
);

-- Operates Relationship Table
CREATE TABLE IF NOT EXISTS Operates (
    AirportID VARCHAR(100),
    AirlineID VARCHAR(100),
    PRIMARY KEY (AirportID, AirlineID),
    FOREIGN KEY (AirportID) REFERENCES Airport(Ap_name),
    FOREIGN KEY (AirlineID) REFERENCES Airline(Airline_ID)
);

INSERT INTO Airport (Ap_name, City, Country) VALUES
('LAX', 'Los Angeles', 'USA'),
('JFK', 'New York', 'USA'),
('DXB', 'Dubai', 'UAE'),
('LHR', 'London', 'UK'),
('HND', 'Tokyo', 'Japan'),
('CDG', 'Paris', 'France'),
('SYD', 'Sydney', 'Australia'),
('FRA', 'Frankfurt', 'Germany'),
('HKG', 'Hong Kong', 'China'),
('SIN', 'Singapore', 'Singapore'),
('LAS', 'Somewhere', 'Somewhat'),
('SEA', 'Underwater', 'Earth');

INSERT INTO Airline (Airline_ID, Airline_name) VALUES
('AN4V82', 'American Airlines'),
('AP9BUR', 'Delta Airlines'),
('AJG2H6', 'Emirates'),
('ATZVOX', 'British Airways'),
('AHX7L2', 'Japan Airlines'),
('AMM4M6', 'Air France'),
('AVCEOV', 'Qantas'),
('A8OFAM', 'Lufthansa'),
('ALK0H6', 'Cathay Pacific'),
('AXVU5Q', 'Singapore Airlines');

INSERT INTO Flight_Employee (Emp_id, F_name, M_name, L_name, Jobtype, Salary, Bdate, Works_For, ManagerID) VALUES
('PLLOIS', 'John', 'M', 'Doe', 'Pilot', 150000, '1983-03-12', 'AN4V82', NULL),
('PL4S0W', 'Jane', NULL, 'Smith', 'Co- Pilot', 120000, '1999-09-11', 'AP9BUR', NULL),
('PL5T6Y', 'Tom', 'A', 'Harris', 'Pilot', 155000, '1985-05-15', 'AN4V82', NULL),
('PL7U8I', 'Emma', 'B', 'Watson', 'Pilot', 160000, '1987-07-17', 'AP9BUR', NULL),
('PL9O0P', 'Chris', 'C', 'Evans', 'Pilot', 165000, '1989-09-19', 'AJG2H6', NULL),
('EFVZ0U', 'Alice', 'B', 'Johnson', 'Cabin Crew', 80000, '1991-11-16', 'AJG2H6', NULL),
('EUR9N2', 'Bob', NULL, 'Brown', 'Cabin Crew', 75000, '1993-12-26', 'ATZVOX', NULL),
('E5XJVL', 'Charlie', 'D', 'Davis', 'Ground Staff', 50000, '1987-03-10', 'AHX7L2', NULL),
('EAWY5N', 'Diana', NULL, 'Miller', 'Ground Staff', 52000, '1985-02-02', 'AMM4M6', NULL),
('E84FB1', 'Grace', 'H', 'Anderson', 'Manager', 90000, '1991-07-14', 'ALK0H6', NULL),
('EQ1SPC', 'Hank', NULL, 'Thomas', 'Manager', 95000, '1996-08-10', 'AXVU5Q', NULL),
('E2J9WF', 'Eve', 'F', 'Wilson', 'Technician', 70000, '1990-04-13', 'AVCEOV', NULL),
('EGBXIG', 'Frank', NULL, 'Taylor', 'Technician', 69000, '1981-10-22', 'A8OFAM', NULL),
('PL1A2B', 'Robert', 'G', 'Downey', 'Pilot', 170000, '1980-04-04', 'AN4V82', NULL),
('PL2C3D', 'Scarlett', 'H', 'Johansson', 'Pilot', 175000, '1984-11-22', 'AP9BUR', NULL),
('PL3E4F', 'Chris', 'I', 'Hemsworth', 'Pilot', 180000, '1983-08-11', 'AJG2H6', NULL),
('PL4G5H', 'Mark', 'J', 'Ruffalo', 'Pilot', 185000, '1967-11-22', 'ATZVOX', NULL),
('PL5I6J', 'Jeremy', 'K', 'Renner', 'Pilot', 190000, '1971-01-07', 'AHX7L2', NULL),
('PL5I2X', 'John', 'D', 'Doe', 'Pilot', 150000, '1980-01-01', 'AN4V82', NULL);


INSERT INTO Employee_Phone (Phone_No, PID) VALUES
('+1-741-3209', 'PLLOIS'),
('+1-572-7187', 'PL4S0W'),
('+1-905-2099', 'EFVZ0U'),
('+1-502-1425', 'EUR9N2'),
('+1-848-3131', 'E5XJVL'),
('+1-994-5231', 'E5XJVL'),
('+1-902-8792', 'EAWY5N'),
('+1-722-4122', 'E2J9WF'),
('+1-353-2272', 'EGBXIG'),
('+1-992-6929', 'E84FB1'),
('+1-112-6384', 'E84FB1'),
('+7-572-1234', 'E84FB1'),
('+1-546-5423', 'EQ1SPC');

INSERT INTO Airplane (AirplaneID, Aircraft_Model, Flying_Hours, SeatingCapacity) VALUES
('A001', 'Boeing 737', 15000.5, 180),
('A002', 'Airbus A320', 12000.0, 160),
('A003', 'Boeing 777', 20000.0, 300),
('A004', 'Airbus A380', 10000.0, 500),
('A005', 'Boeing 787', 18000.0, 250),
('A006', 'Airbus A350', 14000.0, 280),
('A007', 'Boeing 747', 22000.0, 400),
('A008', 'Airbus A330', 16000.0, 290),
('A009', 'Boeing 767', 17000.0, 220),
('A010', 'Airbus A321', 13000.0, 190);

-- Insert data into Flight table
-- Insert data into Flight table
INSERT INTO Flight (Flight_code, Source, Destination, AirplaneID, Pilot, Arrival, Departure) VALUES
('FL001', 'LAX', 'JFK', 'A001', 'PLLOIS', '2023-10-01 08:00:00', '2023-10-01 12:00:00'),
('FL002', 'JFK', 'LAX', 'A002', 'PL4S0W', '2023-10-02 09:00:00', '2023-10-02 13:00:00'),
('FL003', 'DXB', 'LHR', 'A003', 'PL9O0P', '2023-10-03 10:00:00', '2023-10-03 14:00:00'),
('FL004', 'LHR', 'DXB', 'A004', 'PL9O0P', '2023-10-04 11:00:00', '2023-10-04 15:00:00'),
('FL005', 'HND', 'CDG', 'A005', 'PL5I6J', '2023-10-05 12:00:00', '2023-10-05 16:00:00'),
('FL011', 'LAX', 'CDG', 'A010', 'PL5I2X', '2023-04-11 15:00:00', '2023-04-11 22:00:00'),
('FL006', 'CDG', 'HND', 'A002', 'PL5I6J', '2023-10-06 13:00:00', '2023-10-06 17:00:00'),
('FL007', 'SYD', 'FRA', 'A007', 'PL4G5H', '2023-10-07 14:00:00', '2023-10-07 18:00:00'),
('FL008', 'FRA', 'SYD', 'A008', 'PL4G5H', '2023-10-08 15:00:00', '2023-10-08 19:00:00'),
('FL009', 'HKG', 'SIN', 'A009', 'PL1A2B', '2023-10-09 16:00:00', '2023-10-09 20:00:00'),
('FL010', 'SIN', 'HKG', 'A010', 'PL4G5H', '2023-10-10 17:00:00', '2023-10-10 21:00:00'),
('FL012', 'LAX', 'SYD', 'A001', 'PL5I6J', '2023-10-11 08:00:00', '2023-10-11 12:00:00'),
('FL013', 'LAX', 'LAX', 'A003', 'PL4S0W', '2023-10-12 09:00:00', '2023-10-12 13:00:00'),
('FL014', 'LAX', 'SEA', 'A010', 'PL9O0P', '2023-10-13 10:00:00', '2023-10-13 14:00:00'),
('FL015', 'LAX', 'JFK', 'A010', 'PL5I6J', '2023-10-14 11:00:00', '2023-10-14 15:00:00'),
('FL016', 'JFK', 'LAX', 'A005', 'PL4G5H', '2023-10-15 12:00:00', '2023-10-15 16:00:00'),
('FL017', 'JFK', 'SYD', 'A006', 'PL1A2B', '2023-10-16 13:00:00', '2023-10-16 17:00:00'),
('FL018', 'JFK', 'LAX', 'A007', 'PL4S0W', '2023-10-17 14:00:00', '2023-10-17 18:00:00'),
('FL019', 'JFK', 'SEA', 'A009', 'PL9O0P', '2023-10-18 15:00:00', '2023-10-18 19:00:00'),
('FL020', 'JFK', 'DXB', 'A005', 'PL5I6J', '2023-10-19 16:00:00', '2023-10-19 20:00:00'),
('FL021', 'LAX', 'JFK', 'A010', 'PL4G5H', '2023-10-20 17:00:00', '2023-10-20 21:00:00'),
('FL022', 'LAX', 'LAS', 'A003', 'PL1A2B', '2023-10-21 18:00:00', '2023-10-21 22:00:00');

-- Insert data into Passenger table
INSERT INTO Passenger (PID, F_name, M_name, L_name, Bdate, BoardingFlight) VALUES
('P001', 'Michael', 'J', 'Fox', '1985-06-09', 'FL001'),
('P002', 'Sarah', 'K', 'Connor', '1990-07-12', 'FL002'),
('P003', 'James', 'L', 'Bond', '1975-08-15', 'FL003'),
('P004', 'Ellen', 'M', 'Ripley', '1980-09-18', 'FL004'),
('P005', 'John', 'N', 'McClane', '1982-10-21', 'FL005'),
('P006', 'Dana', 'O', 'Scully', '1987-11-24', 'FL006'),
('P007', 'Fox', 'P', 'Mulder', '1983-12-27', 'FL007'),
('P008', 'Clarice', 'Q', 'Starling', '1989-01-30', 'FL008'),
('P009', 'Jack', 'R', 'Ryan', '1984-02-02', 'FL009'),
('P010', 'Jason', 'S', 'Bourne', '1986-03-05', 'FL010'),
('P011', 'Bruce', 'T', 'Wayne', '1972-02-19', 'FL011'),
('P012', 'Clark', 'U', 'Kent', '1978-06-18', 'FL012'),
('P013', 'Diana', 'V', 'Prince', '1981-03-22', 'FL013'),
('P014', 'Barry', 'W', 'Allen', '1985-07-14', 'FL014'),
('P015', 'Arthur', 'X', 'Curry', '1986-01-29', 'FL015'),
('P016', 'Hal', 'Y', 'JSYDan', '1984-11-20', 'FL016'),
('P017', 'Oliver', 'Z', 'Queen', '1983-05-16', 'FL017'),
('P018', 'Victor', 'A', 'Stone', '1987-09-25', 'FL018'),
('P019', 'Billy', 'B', 'Batson', '1990-12-12', 'FL019'),
('P020', 'Kara', 'C', 'Zor-El', '1992-04-10', 'FL020'),
('P021', 'John', 'D', 'Stewart', '1980-08-08', 'FL021'),
('P022', 'Shayera', 'E', 'Hol', '1982-10-30', 'FL022');

-- Insert data into Passenger_Phone table
INSERT INTO Passenger_Phone (Phone_No, PID) VALUES
('+1-123-4567', 'P001'),
('+7-333-9922', 'P001'),
('+1-234-5678', 'P002'),
('+1-345-6789', 'P003'),
('+1-456-7890', 'P004'),
('+1-963-7166', 'P004'),
('+1-567-8901', 'P005'),
('+1-678-9012', 'P006'),
('+1-234-5612', 'P006'),
('+3-100-4112', 'P006'),
('+1-789-0123', 'P007'),
('+1-890-1234', 'P008'),
('+1-901-2345', 'P009'),
('+1-012-3456', 'P010');

-- Insert data into First_Class_Passenger table
INSERT INTO First_Class_Passenger (PID, PrivateSuite, SleepPodAvailability) VALUES
('P001', TRUE, TRUE),
('P002', TRUE, TRUE),
('P003', TRUE, TRUE),
('P004', TRUE, TRUE),
('P005', TRUE, TRUE),
('P006', TRUE, TRUE),
('P007', TRUE, TRUE),
('P008', TRUE, TRUE),
('P009', TRUE, TRUE),
('P010', TRUE, TRUE);

-- Insert data into First_Class_Services table
INSERT INTO First_Class_Services (PID, FirstClassServices) VALUES
('P001', 'Gourmet Meals'),
('P002', 'Personalized Entertainment'),
('P003', 'Luxury Bedding'),
('P004', 'Spa Services'),
('P005', 'Private Chauffeur'),
('P006', 'Gourmet Meals'),
('P007', 'Personalized Entertainment'),
('P008', 'Luxury Bedding'),
('P009', 'Spa Services'),
('P010', 'Private Chauffeur');

-- Insert data into Business_Class_Passenger table
INSERT INTO Business_Class_Passenger (PID, BusinessLoungeAccess, PriorityBoarding, WorkstationAvailability) VALUES
('P001', TRUE, TRUE, TRUE),
('P002', TRUE, TRUE, TRUE),
('P003', TRUE, TRUE, TRUE),
('P004', TRUE, TRUE, TRUE),
('P005', TRUE, TRUE, TRUE),
('P006', TRUE, TRUE, TRUE),
('P007', TRUE, TRUE, TRUE),
('P008', TRUE, TRUE, TRUE),
('P009', TRUE, TRUE, TRUE),
('P010', TRUE, TRUE, TRUE);

-- Insert data into Business_Class_Services table
INSERT INTO Business_Class_Services (PID, BusinessClassServices) VALUES
('P001', 'Priority Check-in'),
('P002', 'Extra Legroom'),
('P003', 'In-flight Wi-Fi'),
('P004', 'Priority Check-in'),
('P005', 'Extra Legroom'),
('P006', 'In-flight Wi-Fi'),
('P007', 'Priority Check-in'),
('P008', 'Extra Legroom'),
('P009', 'In-flight Wi-Fi'),
('P010', 'Priority Check-in');

-- Insert data into Dependents table
INSERT INTO Dependents (Name, DOB, Relationship, Depends_on) VALUES
('Anna', '2010-05-10', 'Daughter', 'PLLOIS'),
('Ben', '2012-07-15', 'Son', 'PL4S0W'),
('Cathy', '2014-09-20', 'Daughter', 'EFVZ0U'),
('David', '2016-11-25', 'Son', 'EUR9N2'),
('Eva', '2018-01-30', 'Daughter', 'E5XJVL'),
('Frank', '2020-03-05', 'Son', 'EAWY5N'),
('Grace', '2022-05-10', 'Daughter', 'E2J9WF'),
('Hank', '2024-07-15', 'Son', 'EGBXIG'),
('Ivy', '2026-09-20', 'Daughter', 'E84FB1'),
('Jack', '2028-11-25', 'Son', 'EQ1SPC');

-- Insert data into Baggage table
INSERT INTO Baggage (BaggageId, Weight, BelongsTo) VALUES
('B01', 23.5, 'P001'),
('B02', 25.0, 'P002'),
('B03', 22.0, 'P003'),
('B04', 24.5, 'P004'),
('B05', 26.0, 'P005'),
('B06', 23.0, 'P006'),
('B07', 25.5, 'P007'),
('B08', 22.5, 'P008'),
('B09', 24.0, 'P009'),
('B10', 26.5, 'P010');

-- Insert data into Operates table
INSERT INTO Operates (AirportID, AirlineID) VALUES
('LAX', 'AN4V82'),
('JFK', 'AP9BUR'),
('DXB', 'AJG2H6'),
('LHR', 'ATZVOX'),
('HND', 'AHX7L2'),
('CDG', 'AMM4M6'),
('SYD', 'AVCEOV'),
('FRA', 'A8OFAM'),
('HKG', 'ALK0H6'),
('SIN', 'AXVU5Q');
/* SELECT CONCAT('DESCRIBE ', table_name, ';') AS describe_command
FROM information_schema.tables
WHERE table_schema = 'AIRLINE */