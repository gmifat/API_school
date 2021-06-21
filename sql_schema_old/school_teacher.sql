-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: school
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(55) NOT NULL,
  `last_name` varchar(55) NOT NULL,
  `grade` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'prof1_fn','prof1-ln','professeur','hj@mail.com','0606060606','46 rue de l\'ecole 75002 Paris'),(2,'prof2_fn','prof2-ln','maitre de conférence','hkf@mail.com','090904040','498 rue de l\'ecole 75001 Paris'),(3,'prof3_fn','prof3_ln','maître assistant habilité','uj@mail.com','0101010101','46 rue de l\'ecole 75003 Paris'),(4,'prof4_fn','prof4_ln','maître assistant ','hy@mail.com','09090909','48 rue de l\'ecole 75011 Paris'),(6,'prof5_fn','prof5_ln','professeur','hf@mail.com','0404040404','18 rue de l\'université 75001 Paris'),(8,'prof6_fn','prof6_ln','professeur','prof6@mail.com','0505050505','55 rue de l\'école 75000 Paris'),(9,'prof9_ln','prof9','professeur','prof9@mail.com','0707070707','34 rue'),(11,'ggg','ggg','ggg','ggg','ggg','ggg'),(13,'qqqq','qqqq','qqq','qqq','qqqq','qqq'),(14,'llll','lllll','llll','llll','lllll','llll'),(15,'teacher15','teacher15','professeur','teacher15@mail.com','qqqq','uu'),(16,'ftgf','fghfg','gfgh','fgdfh','ghfg','gh'),(17,'Mrad','fatma','professeur','fatma@mail.com','04040404040','32 rue de mathématiques '),(18,'dhrifa_ln','dhrifa_fn','docteur informatique ','dhrifa@mail.com','090909090','23 rur de l\'informatique');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-04 12:40:48
