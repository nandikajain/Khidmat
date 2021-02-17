-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: khidmatDB
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Contains`
--

DROP TABLE IF EXISTS `Contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contains` (
  `foodID` varchar(8) DEFAULT NULL,
  `orderID` varchar(8) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  KEY `foodID` (`foodID`),
  KEY `orderID` (`orderID`),
  CONSTRAINT `Contains_ibfk_1` FOREIGN KEY (`foodID`) REFERENCES `Food` (`itemID`),
  CONSTRAINT `Contains_ibfk_2` FOREIGN KEY (`orderID`) REFERENCES `Orders` (`orderID`),
  CONSTRAINT `Contains_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contains`
--

LOCK TABLES `Contains` WRITE;
/*!40000 ALTER TABLE `Contains` DISABLE KEYS */;
/*!40000 ALTER TABLE `Contains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `phone` char(10) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `email` varchar(50) NOT NULL,
  `customerType` varchar(20) NOT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`phone`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  CONSTRAINT `typeContraint` CHECK (((`customerType` = _utf8mb4'normal') or (`customerType` = _utf8mb4'premium')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DeliveryWorker`
--

DROP TABLE IF EXISTS `DeliveryWorker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DeliveryWorker` (
  `employeeId` varchar(8) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `phone` char(10) NOT NULL,
  `salary` int DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `socialCause` tinyint(1) NOT NULL DEFAULT '0',
  `tips` int NOT NULL DEFAULT '0',
  `supervisorID` varchar(8) DEFAULT NULL,
  `fuelAmt` int DEFAULT '2000',
  PRIMARY KEY (`employeeId`),
  UNIQUE KEY `phone` (`phone`),
  KEY `supervisorID` (`supervisorID`),
  CONSTRAINT `DeliveryWorker_ibfk_1` FOREIGN KEY (`supervisorID`) REFERENCES `Management` (`employeeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DeliveryWorker`
--

LOCK TABLES `DeliveryWorker` WRITE;
/*!40000 ALTER TABLE `DeliveryWorker` DISABLE KEYS */;
/*!40000 ALTER TABLE `DeliveryWorker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Donation`
--

DROP TABLE IF EXISTS `Donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Donation` (
  `donationID` varchar(8) NOT NULL,
  `donorID` varchar(8) NOT NULL,
  `receiverID` varchar(8) DEFAULT NULL,
  `deliveryWorkerID` varchar(8) NOT NULL,
  `dateTime` datetime DEFAULT NULL,
  `category` varchar(10) NOT NULL,
  `status` varchar(8) DEFAULT NULL,
  `quantity` int DEFAULT (1),
  PRIMARY KEY (`donationID`),
  KEY `donorID` (`donorID`),
  KEY `receiverID` (`receiverID`),
  KEY `deliveryWorkerID` (`deliveryWorkerID`),
  CONSTRAINT `Donation_ibfk_1` FOREIGN KEY (`donorID`) REFERENCES `Donor` (`donorId`),
  CONSTRAINT `Donation_ibfk_2` FOREIGN KEY (`receiverID`) REFERENCES `Receiver` (`receiverId`),
  CONSTRAINT `Donation_ibfk_3` FOREIGN KEY (`deliveryWorkerID`) REFERENCES `DeliveryWorker` (`employeeId`),
  CONSTRAINT `Donation_chk_1` CHECK (((`category` = _utf8mb4'Food') or (`category` = _utf8mb4'Clothes') or (`category` = _utf8mb4'Money'))),
  CONSTRAINT `Donation_chk_2` CHECK (((`status` = _utf8mb4'active') or (`status` = _utf8mb4'delivered')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donation`
--

LOCK TABLES `Donation` WRITE;
/*!40000 ALTER TABLE `Donation` DISABLE KEYS */;
/*!40000 ALTER TABLE `Donation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Donor`
--

DROP TABLE IF EXISTS `Donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Donor` (
  `donorId` varchar(8) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `points` int DEFAULT '0',
  PRIMARY KEY (`donorId`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donor`
--

LOCK TABLES `Donor` WRITE;
/*!40000 ALTER TABLE `Donor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Food`
--

DROP TABLE IF EXISTS `Food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Food` (
  `itemID` varchar(8) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` decimal(4,2) NOT NULL,
  `isAvailable` tinyint(1) DEFAULT NULL,
  `imagePath` varchar(200) DEFAULT NULL,
  `isVeg` tinyint(1) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `discount` int DEFAULT '0',
  `restaurantID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`itemID`),
  KEY `restaurantID` (`restaurantID`),
  CONSTRAINT `Food_ibfk_1` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Food_chk_1` CHECK (((`category` = _utf8mb4'Dessert') or (`category` = _utf8mb4'Main Course') or (`category` = _utf8mb4'Beverage') or (`category` = _utf8mb4'Starter')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Food`
--

LOCK TABLES `Food` WRITE;
/*!40000 ALTER TABLE `Food` DISABLE KEYS */;
/*!40000 ALTER TABLE `Food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Management`
--

DROP TABLE IF EXISTS `Management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Management` (
  `employeeId` varchar(8) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `phone` char(10) NOT NULL,
  `salary` int DEFAULT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `dob` date DEFAULT NULL,
  `supervisorID` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`employeeId`),
  UNIQUE KEY `phone` (`phone`),
  KEY `supervisorID` (`supervisorID`),
  CONSTRAINT `Management_ibfk_1` FOREIGN KEY (`supervisorID`) REFERENCES `Management` (`employeeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Management`
--

LOCK TABLES `Management` WRITE;
/*!40000 ALTER TABLE `Management` DISABLE KEYS */;
/*!40000 ALTER TABLE `Management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `orderID` varchar(8) NOT NULL,
  `status` varchar(8) NOT NULL,
  `dateTime` datetime DEFAULT NULL,
  `billAmt` decimal(6,2) DEFAULT NULL,
  `paymentMode` varchar(10) DEFAULT NULL,
  `customerID` varchar(8) DEFAULT NULL,
  `restaurantID` varchar(8) DEFAULT NULL,
  `deliveryWorkerID` varchar(8) DEFAULT NULL,
  `discount` int DEFAULT '0',
  `tip` decimal(5,2) DEFAULT (0),
  PRIMARY KEY (`orderID`),
  KEY `customerID` (`customerID`),
  KEY `restaurantID` (`restaurantID`),
  KEY `deliveryWorkerID` (`deliveryWorkerID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`phone`),
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Orders_ibfk_3` FOREIGN KEY (`deliveryWorkerID`) REFERENCES `DeliveryWorker` (`employeeId`),
  CONSTRAINT `Orders_chk_1` CHECK (((`status` = _utf8mb4'active') or (`status` = _utf8mb4'delivered')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rates`
--

DROP TABLE IF EXISTS `Rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rates` (
  `ratings` int DEFAULT NULL,
  `customerID` char(10) NOT NULL,
  `restaurantID` varchar(8) NOT NULL,
  KEY `customerID` (`customerID`),
  KEY `restaurantID` (`restaurantID`),
  CONSTRAINT `Rates_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`phone`),
  CONSTRAINT `Rates_ibfk_2` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Rates_chk_1` CHECK (((`ratings` > 0) and (`ratings` < 6)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rates`
--

LOCK TABLES `Rates` WRITE;
/*!40000 ALTER TABLE `Rates` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Receiver`
--

DROP TABLE IF EXISTS `Receiver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receiver` (
  `receiverId` varchar(8) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `accepts` varchar(20) NOT NULL,
  PRIMARY KEY (`receiverId`),
  UNIQUE KEY `phone` (`phone`),
  CONSTRAINT `Receiver_chk_1` CHECK (((`accepts` = _utf8mb4'Meals') or (`accepts` = _utf8mb4'Money') or (`accepts` = _utf8mb4'Clothes')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receiver`
--

LOCK TABLES `Receiver` WRITE;
/*!40000 ALTER TABLE `Receiver` DISABLE KEYS */;
/*!40000 ALTER TABLE `Receiver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Restaurant`
--

DROP TABLE IF EXISTS `Restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Restaurant` (
  `restaurantID` varchar(10) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `dayOfOpening` date DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `area` varchar(20) NOT NULL,
  PRIMARY KEY (`restaurantID`),
  CONSTRAINT `Restaurant_chk_1` CHECK (((`type` = _utf8mb4'South Indian') or (`type` = _utf8mb4'Mexican') or (`type` = _utf8mb4'Continental') or (`type` = _utf8mb4'Fast Food') or (`type` = _utf8mb4'Mughlai')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Restaurant`
--

LOCK TABLES `Restaurant` WRITE;
/*!40000 ALTER TABLE `Restaurant` DISABLE KEYS */;
/*!40000 ALTER TABLE `Restaurant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-17 23:55:14
