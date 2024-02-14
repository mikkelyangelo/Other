-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
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
-- Table structure for table `medicalentry`
--

DROP TABLE IF EXISTS `medicalentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicalentry` (
  `me_id` int NOT NULL AUTO_INCREMENT,
  `date_entry` varchar(45) NOT NULL,
  `survs` varchar(45) DEFAULT NULL,
  `appointms` varchar(45) DEFAULT NULL,
  `mc_id` int NOT NULL,
  `doc_id` int NOT NULL,
  PRIMARY KEY (`me_id`),
  KEY `mc_id_idx` (`mc_id`),
  KEY `dc_id_idx` (`doc_id`),
  CONSTRAINT `dc_id` FOREIGN KEY (`doc_id`) REFERENCES `doctor` (`doc_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `mc_id` FOREIGN KEY (`mc_id`) REFERENCES `medicalcard` (`mc_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicalentry`
--

LOCK TABLES `medicalentry` WRITE;
/*!40000 ALTER TABLE `medicalentry` DISABLE KEYS */;
INSERT INTO `medicalentry` VALUES (1,'2020-09-10',NULL,NULL,1,3),(2,'2020-04-01',NULL,NULL,2,4);
/*!40000 ALTER TABLE `medicalentry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-18 20:23:42
