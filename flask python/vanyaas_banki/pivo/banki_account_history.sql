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
-- Table structure for table `account_history`
--

DROP TABLE IF EXISTS `account_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_history` (
  `idaccount_history` int NOT NULL AUTO_INCREMENT,
  `account_id` int NOT NULL,
  `old_balance` varchar(45) NOT NULL,
  `new_balance` varchar(45) NOT NULL,
  `balance_date` varchar(45) NOT NULL,
  `reason` varchar(45) NOT NULL,
  PRIMARY KEY (`idaccount_history`),
  KEY `FK_account_id_idx` (`account_id`),
  CONSTRAINT `FK_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`idaccount`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_history`
--

LOCK TABLES `account_history` WRITE;
/*!40000 ALTER TABLE `account_history` DISABLE KEYS */;
INSERT INTO `account_history` VALUES (1,5,'6053','5985','2023-04-06 22:43:47','Deposit/Withdrawal/Transfer'),(2,2,'3581','5430','2023-04-06 22:43:49','Deposit/Withdrawal/Transfer'),(3,4,'7316','8843','2023-04-06 22:43:49','Deposit/Withdrawal/Transfer'),(4,5,'8702','9809','2023-04-06 22:43:50','Deposit/Withdrawal/Transfer'),(5,1,'2322','1956','2023-04-06 22:43:50','Deposit/Withdrawal/Transfer'),(6,1,'7370','7270','2023-04-06 23:11:25','transfer'),(7,2,'9148.302004402785','9302.60400880557','2023-04-06 23:11:25','transfer'),(8,1,'7270','7170','2023-04-06 23:11:44','transfer'),(9,2,'9302.60400880557','9456.906013208356','2023-04-06 23:11:44','transfer'),(10,1,'7170','7070','2023-04-06 23:11:45','transfer'),(11,2,'9456.906013208356','9611.208017611141','2023-04-06 23:11:45','transfer'),(12,1,'7070','6970','2023-04-20 15:23:27','transfer'),(13,2,'9611.208017611141','9765.510022013927','2023-04-20 15:23:27','transfer'),(14,1,'6970','6870','2023-04-20 15:23:30','transfer'),(15,2,'9765.510022013927','9919.812026416712','2023-04-20 15:23:30','transfer'),(16,1,'6870','6770','2023-04-20 15:24:22','transfer'),(17,2,'9919.812026416712','10074.114030819497','2023-04-20 15:24:22','transfer'),(18,3,'1271','951','2023-04-20 15:40:16','transfer'),(19,4,'7690.770855298983','8513.541710597967','2023-04-20 15:40:16','transfer'),(20,4,'6975.770855298983','6260.770855298983','2023-04-20 15:41:22','transfer'),(21,2,'11758.190656225379','13596.569286034046','2023-04-20 15:41:22','transfer'),(22,4,'6675.770855298983','6375.770855298983','2023-04-20 15:42:48','transfer'),(23,2,'12126.21101925449','12494.2313822836','2023-04-20 15:42:48','transfer');
/*!40000 ALTER TABLE `account_history` ENABLE KEYS */;
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
