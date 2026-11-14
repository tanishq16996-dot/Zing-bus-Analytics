CREATE DATABASE zingbus;
USE zingbus;

CREATE TABLE customers(
CustomerID INT PRIMARY KEY,
CustomerName VARCHAR(100),
Age INT,
Gender VARCHAR(20),
City VARCHAR(50),
SignupDate DATE
);

CREATE TABLE routes(
RouteID INT PRIMARY KEY,
Source VARCHAR(50),
Destination VARCHAR(50),
DistanceKM INT
);

CREATE TABLE buses(
BusID INT PRIMARY KEY,
BusType VARCHAR(50),
Capacity INT
);

CREATE TABLE bookings(
BookingID INT PRIMARY KEY,
CustomerID INT,
BusID INT,
RouteID INT,
JourneyDate DATE,
Fare DECIMAL(10,2),
Discount DECIMAL(10,2),
Rating INT,
Status VARCHAR(20),
NetFare DECIMAL(10,2)
);

-- Example Analysis

SELECT City,COUNT(*) TotalCustomers
FROM customers
GROUP BY City;

SELECT r.Source,r.Destination,
SUM(b.NetFare) Revenue
FROM bookings b
JOIN routes r
ON b.RouteID=r.RouteID
GROUP BY r.Source,r.Destination
ORDER BY Revenue DESC;

SELECT AVG(NetFare) AvgFare
FROM bookings;

SELECT Status,COUNT(*) TotalBookings
FROM bookings
GROUP BY Status;
