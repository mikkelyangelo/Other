-- MySQL dump 10.13  Distrib 8.0.32, for macos13.0 (arm64)
--
-- Host: localhost    Database: Kostevko_rk6
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `commission`
--

DROP TABLE IF EXISTS `commission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commission` (
  `id` int NOT NULL,
  `commission_number` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `commission_number` (`commission_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commission`
--

LOCK TABLES `commission` WRITE;
/*!40000 ALTER TABLE `commission` DISABLE KEYS */;
INSERT INTO `commission` VALUES (1,101),(2,102),(3,103),(4,104);
/*!40000 ALTER TABLE `commission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commission_teacher`
--

DROP TABLE IF EXISTS `commission_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commission_teacher` (
  `commission_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  PRIMARY KEY (`commission_id`,`teacher_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `commission_teacher_ibfk_1` FOREIGN KEY (`commission_id`) REFERENCES `commission` (`id`),
  CONSTRAINT `commission_teacher_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commission_teacher`
--

LOCK TABLES `commission_teacher` WRITE;
/*!40000 ALTER TABLE `commission_teacher` DISABLE KEYS */;
INSERT INTO `commission_teacher` VALUES (1,1),(4,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4);
/*!40000 ALTER TABLE `commission_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `defense_protocol`
--

DROP TABLE IF EXISTS `defense_protocol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `defense_protocol` (
  `id` int NOT NULL,
  `project_id` int DEFAULT NULL,
  `grade` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `defense_protocol_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `defense_protocol`
--

LOCK TABLES `defense_protocol` WRITE;
/*!40000 ALTER TABLE `defense_protocol` DISABLE KEYS */;
INSERT INTO `defense_protocol` VALUES (1,1,3),(2,2,4),(3,3,5),(4,4,3),(5,5,4),(6,6,3),(7,7,5),(8,8,5);
/*!40000 ALTER TABLE `defense_protocol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `defense_schedule`
--

DROP TABLE IF EXISTS `defense_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `defense_schedule` (
  `id` int NOT NULL,
  `date_sh` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `room` varchar(255) DEFAULT NULL,
  `commission_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `commission_id` (`commission_id`),
  CONSTRAINT `defense_schedule_ibfk_1` FOREIGN KEY (`commission_id`) REFERENCES `commission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `defense_schedule`
--

LOCK TABLES `defense_schedule` WRITE;
/*!40000 ALTER TABLE `defense_schedule` DISABLE KEYS */;
INSERT INTO `defense_schedule` VALUES (1,'2023-04-04','10:00:00','417',1),(2,'2023-04-05','11:00:00','520',2),(3,'2013-03-11','12:00:00','123',3),(4,'2013-03-18','13:00:00','220л',4),(5,'2023-04-04','10:00:00','417',2),(6,'2020-06-05','11:00:00','520',2),(7,'2020-05-11','12:00:00','123',2),(8,'2020-05-18','13:00:00','220л',4);
/*!40000 ALTER TABLE `defense_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` int NOT NULL,
  `theme` varchar(255) DEFAULT NULL,
  `defense_date` date DEFAULT NULL,
  `grade` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Исследование источников тока','2023-04-04',3),(2,'Исследование шурупов','2023-04-05',4),(3,'Программирование','2013-03-11',5),(4,'Нейросети','2013-03-18',3),(5,'Технологии','2020-05-04',4),(6,'Химия','2020-09-08',3),(7,'История','2020-05-02',5),(8,'Право','2020-11-11',5);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_student`
--

DROP TABLE IF EXISTS `project_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_student` (
  `project_id` int NOT NULL,
  `student_id` int NOT NULL,
  `teacher_id` int DEFAULT NULL,
  PRIMARY KEY (`project_id`,`student_id`),
  KEY `student_id` (`student_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `project_student_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `project_student_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`),
  CONSTRAINT `project_student_ibfk_3` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_student`
--

LOCK TABLES `project_student` WRITE;
/*!40000 ALTER TABLE `project_student` DISABLE KEYS */;
INSERT INTO `project_student` VALUES (1,1,1),(1,2,1),(2,2,2),(2,3,2),(5,1,2),(6,2,2),(3,3,3),(3,4,3),(7,3,3),(8,1,3),(4,1,4),(4,4,4);
/*!40000 ALTER TABLE `project_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `student_card_number` int DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_card_number` (`student_card_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,12345,'Иванов','2002-01-01','Группа 1'),(2,67890,'Петров','2001-03-05','Группа 2'),(3,13579,'Сидоров','2000-05-10','Группа 1'),(4,24680,'Кузнецов','2003-08-15','Группа 3');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` int NOT NULL,
  `teacher_number` int DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `employment_date` date DEFAULT NULL,
  `department_code` varchar(255) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `disemployment_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teacher_number` (`teacher_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,1001,'Смирнов','1975-02-10','2013-03-02','РК6','Доцент',NULL),(2,1002,'Иванова','1980-06-15','2013-03-03','ФН1','Профессор',NULL),(3,1003,'Петрова','1978-11-20','2003-09-01','МТ5','Магистр',NULL),(4,1004,'Сидорова','1985-03-25','2013-03-01','ИУ8','Доцент',NULL),(5,1045,'Васильев','1975-02-10','2000-09-01','РК6','Доцент',NULL),(6,1051,'Уральцев','1994-02-10','2010-09-01','РК9','Аспирант',NULL);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `teacher_excellent_project_count`
--

DROP TABLE IF EXISTS `teacher_excellent_project_count`;
/*!50001 DROP VIEW IF EXISTS `teacher_excellent_project_count`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `teacher_excellent_project_count` AS SELECT 
 1 AS `teacher_id`,
 1 AS `excellent_project_count`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `teacher_excellent_project_count`
--

/*!50001 DROP VIEW IF EXISTS `teacher_excellent_project_count`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `teacher_excellent_project_count` AS select `ps`.`teacher_id` AS `teacher_id`,count(0) AS `excellent_project_count` from (`project_student` `ps` join `defense_protocol` `dp` on((`dp`.`project_id` = `ps`.`project_id`))) where (`dp`.`grade` = 5) group by `ps`.`teacher_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-06  2:14:12