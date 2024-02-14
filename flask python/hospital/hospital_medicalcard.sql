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
-- Table structure for table `medicalcard`
--

DROP TABLE IF EXISTS `medicalcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicalcard` (
  `mc_id` int NOT NULL AUTO_INCREMENT,
  `passport_p` varchar(45) NOT NULL,
  `FCs_p` varchar(45) NOT NULL,
  `adress_p` varchar(45) DEFAULT NULL,
  `birthday_p` date DEFAULT NULL,
  `diagnosis` varchar(45) NOT NULL,
  `date_of_ad` date NOT NULL,
  `date_of_discharge` date DEFAULT NULL,
  `w_id` int NOT NULL,
  `doc_id` int NOT NULL,
  PRIMARY KEY (`mc_id`),
  KEY `w_id_idx` (`w_id`),
  KEY `doc_id_idx` (`doc_id`),
  CONSTRAINT `doc_id` FOREIGN KEY (`doc_id`) REFERENCES `doctor` (`doc_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `w_id` FOREIGN KEY (`w_id`) REFERENCES `ward` (`w_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicalcard`
--

LOCK TABLES `medicalcard` WRITE;
/*!40000 ALTER TABLE `medicalcard` DISABLE KEYS */;
INSERT INTO `medicalcard` VALUES (1,'8513660718','Фёдоров М.С.','Москва','2002-03-12','миакардия','2020-10-08','2020-10-19',3,4),(2,'8513660719','Носов И.К.','Москва','2003-12-23','грипп','2020-03-30','2020-04-06',1,1),(3,'8513660714','Соловьев М.Ю.','Уфа','2004-02-27','разрыв сетчатки','2023-03-22',NULL,2,2),(4,'8513660713','Романова А.Т.','Москва','2001-10-03','ОРВИ','2023-03-12','2023-03-23',4,3),(5,'8513660816','Сергеев И.А.','Москва','1998-11-30','ОРВИ','2023-03-27',NULL,4,3),(6,'8513660817','Семенов Р.Г.','Уфа','2000-03-27','грипп','2020-10-27',NULL,3,4),(7,'8513660818','Семенов Ф.А.','Москва',NULL,'ОРВИ','2023-03-20',NULL,4,3);
/*!40000 ALTER TABLE `medicalcard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-18 20:23:39
