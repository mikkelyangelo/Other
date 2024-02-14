-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: rk6_shema
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `birth_date` date NOT NULL,
  `adress` varchar(45) NOT NULL,
  `education` varchar(45) NOT NULL,
  `job_id` int NOT NULL,
  `salary` float NOT NULL,
  `enrollment_date` date NOT NULL,
  `dismissal_date` date DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `job_id_idx` (`job_id`),
  KEY `employee_staffing_idx` (`job_id`),
  CONSTRAINT `employee_staffing` FOREIGN KEY (`job_id`) REFERENCES `staffing` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'John','1989-05-13','Moscow','middle',3,85000,'2007-07-29','2015-04-23'),(2,'Macy','1995-10-30','Barcelona','high',1,27000,'2020-03-11','2021-05-15'),(3,'Boris','2000-01-04','Mexico','middle',9,150000,'2020-11-26','2022-12-01'),(4,'Turik','2002-08-20','Baku','high',5,777777,'2014-03-04','2018-05-05'),(5,'Trisha','1985-12-02','Barcelona','high',1,84000,'2020-05-12','2020-03-15'),(6,'Anuka','1999-07-25','Tokyo','magistracy',2,133000,'2023-03-25','2023-01-23'),(7,'Morty','2000-04-03','Mexico','high',8,65000,'2020-03-01',NULL),(8,'sasha','2002-04-04','moskva','high',3,85000,'2021-05-21',NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-23 19:50:23
