-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: banki
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
-- Table structure for table `transfer_history`
--

DROP TABLE IF EXISTS `transfer_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transfer_history` (
  `idtransfer_history` int NOT NULL AUTO_INCREMENT,
  `source_account_id` int NOT NULL,
  `destination_account_id` int NOT NULL,
  `transfer_amount` varchar(45) NOT NULL,
  `exchange_rate_id` int NOT NULL,
  `transfer_date` varchar(45) NOT NULL,
  PRIMARY KEY (`idtransfer_history`),
  KEY `FK_exchange_rate_id_idx` (`exchange_rate_id`),
  KEY `FK_source_account_id_idx` (`source_account_id`),
  KEY `FK_destination_account_id_idx` (`destination_account_id`),
  CONSTRAINT `FK_destination_account_id` FOREIGN KEY (`destination_account_id`) REFERENCES `account` (`idaccount`),
  CONSTRAINT `FK_exchange_rate_id` FOREIGN KEY (`exchange_rate_id`) REFERENCES `exchange_rate` (`idexchange_rate`),
  CONSTRAINT `FK_source_account_id` FOREIGN KEY (`source_account_id`) REFERENCES `account` (`idaccount`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfer_history`
--

LOCK TABLES `transfer_history` WRITE;
/*!40000 ALTER TABLE `transfer_history` DISABLE KEYS */;
INSERT INTO `transfer_history` VALUES (1,2,1,'661',5,'2023-05-06 22:45:14'),(2,5,2,'493',4,'2023-04-06 22:45:15'),(3,2,5,'434',2,'2023-04-06 22:45:16'),(4,3,4,'320',2,'2023-04-06 22:45:16'),(5,2,4,'654',3,'2023-04-06 22:45:17'),(8,1,2,'100.00',1,'2023-04-06 23:11:25'),(9,1,2,'100.00',1,'2023-04-06 23:11:44'),(10,1,2,'100.00',1,'2023-04-06 23:11:45'),(15,1,2,'100.00',1,'2023-04-20 15:23:27'),(16,1,2,'100.00',1,'2023-04-20 15:23:30'),(17,1,2,'100.00',1,'2023-04-20 15:24:22'),(19,5,1,'100',1,'2023-04-20 15:25:45'),(20,4,3,'910',4,'2023-04-20 15:25:47'),(21,5,2,'100',2,'2023-04-20 15:25:47'),(22,3,4,'337',5,'2023-04-20 15:25:47'),(23,4,2,'715',2,'2023-04-20 15:25:47'),(24,4,2,'300.00',3,'2023-04-20 15:42:48');
/*!40000 ALTER TABLE `transfer_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-21 20:38:53
