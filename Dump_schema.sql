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
-- Table structure for table `administration`
--

DROP TABLE IF EXISTS `administration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administration` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(55) NOT NULL,
  `last_name` varchar(55) NOT NULL,
  `role` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administration`
--

LOCK TABLES `administration` WRITE;
/*!40000 ALTER TABLE `administration` DISABLE KEYS */;
INSERT INTO `administration` VALUES (1,'admin1','admin1_ln','assist_admin','admin1@mail.com','0909090909','23 rue de l\'administration 75005 Paris'),(2,'admin2','admin2_ln','assistant','admin2@gmail.com','0404040404','876 rue de l\'admin 78000 Versailles'),(4,'admin3','admin3_ln','agent d\'acceuil','admin3@mail.com','0202020202','65 rue de l\'admin 75006 Paris'),(5,'admin4','admin4_fn','agent d\'acceuil','admin4@mail.com','0505050505','54 rue de de l\'administration 75000 paris');
/*!40000 ALTER TABLE `administration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `class_id` int NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'Master1'),(2,'Masterhjh'),(3,'Bac'),(4,'terminal'),(5,'Prépa'),(6,'Médecine');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_session`
--

DROP TABLE IF EXISTS `class_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_session` (
  `class_session_id` int NOT NULL AUTO_INCREMENT,
  `speciality_id` int NOT NULL,
  `class_subject_id` int NOT NULL,
  `classroom_id` int DEFAULT NULL,
  `day` date NOT NULL,
  `start_time` int NOT NULL,
  `duration` int NOT NULL,
  `virtuel` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`class_session_id`),
  KEY `fk_class_session_speciality_id_idx` (`speciality_id`),
  KEY `fk_class_session_classroom_id_idx` (`classroom_id`),
  KEY `fk_class_session_class_subject_id_idx` (`class_subject_id`),
  CONSTRAINT `fk_class_session_class_subject_id` FOREIGN KEY (`class_subject_id`) REFERENCES `class_subject` (`class_subject_id`),
  CONSTRAINT `fk_class_session_classroom_id` FOREIGN KEY (`classroom_id`) REFERENCES `classroom` (`classroom_id`),
  CONSTRAINT `fk_class_session_speciality_id` FOREIGN KEY (`speciality_id`) REFERENCES `speciality` (`speciality_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_session`
--

LOCK TABLES `class_session` WRITE;
/*!40000 ALTER TABLE `class_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `class_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_subject`
--

DROP TABLE IF EXISTS `class_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_subject` (
  `class_subject_id` int NOT NULL AUTO_INCREMENT,
  `class_id` int NOT NULL,
  `subject_id` int NOT NULL,
  PRIMARY KEY (`class_subject_id`),
  KEY `fk_class_subject_class_id_idx` (`class_id`),
  KEY `fk_class_subject_subject_id_idx` (`subject_id`),
  CONSTRAINT `fk_class_subject_class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  CONSTRAINT `fk_class_subject_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_subject`
--

LOCK TABLES `class_subject` WRITE;
/*!40000 ALTER TABLE `class_subject` DISABLE KEYS */;
/*!40000 ALTER TABLE `class_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classroom`
--

DROP TABLE IF EXISTS `classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classroom` (
  `classroom_id` int NOT NULL AUTO_INCREMENT,
  `room_number` varchar(45) NOT NULL,
  PRIMARY KEY (`classroom_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classroom`
--

LOCK TABLES `classroom` WRITE;
/*!40000 ALTER TABLE `classroom` DISABLE KEYS */;
INSERT INTO `classroom` VALUES (1,'salle1'),(2,'salle2'),(3,'salle3'),(4,'salle4'),(5,'salle5'),(6,'salle6'),(7,'salle7'),(8,'salle8'),(9,'salle9');
/*!40000 ALTER TABLE `classroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mark`
--

DROP TABLE IF EXISTS `mark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mark` (
  `mark_id` int NOT NULL AUTO_INCREMENT,
  `score_value` varchar(255) NOT NULL,
  `student_id` int NOT NULL,
  `subject_id` int NOT NULL,
  PRIMARY KEY (`mark_id`),
  KEY `fk_mark_student_id_idx` (`student_id`),
  KEY `fk_mark_subject_id_idx` (`subject_id`),
  CONSTRAINT `fk_mark_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  CONSTRAINT `fk_mark_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mark`
--

LOCK TABLES `mark` WRITE;
/*!40000 ALTER TABLE `mark` DISABLE KEYS */;
/*!40000 ALTER TABLE `mark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `person_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'prof1','prof1_ln','hs@mail.com','0909090909',NULL),(2,'prof2','proff2 ln','gh@mail.com','0606060606','23 rue de l\'ecole 75001 Paris'),(3,'prof3','prof3_ln','kj@mail.com','0707070707','27 rue de l\'ecole 75002 Paris'),(4,'prof4','prof4_ln','jh@mail.com','0808080808','37 rue de l\'école');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speciality`
--

DROP TABLE IF EXISTS `speciality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `speciality` (
  `speciality_id` int NOT NULL AUTO_INCREMENT,
  `teacher_id` int NOT NULL,
  `subject_id` int NOT NULL,
  PRIMARY KEY (`speciality_id`),
  KEY `fk_speciality_teacher_id_idx` (`teacher_id`),
  KEY `fspeciality_ subject_id_idx` (`subject_id`),
  CONSTRAINT `fk_speciality_ subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`),
  CONSTRAINT `fk_speciality_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speciality`
--

LOCK TABLES `speciality` WRITE;
/*!40000 ALTER TABLE `speciality` DISABLE KEYS */;
INSERT INTO `speciality` VALUES (1,14,1),(2,14,5),(3,15,3),(4,15,5),(5,16,3),(6,16,5),(7,17,5),(8,17,9),(9,17,12),(10,18,1),(11,18,2),(12,18,4),(13,18,6),(14,18,12);
/*!40000 ALTER TABLE `speciality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `card_number` varchar(255) DEFAULT NULL,
  `class_id` int NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `fk_class_id_idx` (`class_id`),
  CONSTRAINT `fk_student_class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (2,'etudiant3','etudiant2_ln','4567709',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(3,'etudiant4','etudiant2_ln','7845677',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(7,'etudiant3','etudiant3_ln','45677',3,'etudiant3@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(8,'etudiant2','etudiant2_ln','45677',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(9,'etudiant2','etudiant2_ln','45677',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(10,'etudiant5','etudiant5_ln','4567765',3,'etudiant5@mail.com','0909090909','98 rue de l\'étudiant 87000 Paris'),(11,'etudiant2','etudiant2_ln','45677',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(12,'etudiant2','etudiant2_ln','45677',2,'etudiant2@mail.com','0909090909','33 rue de l\'étudiant 87000 Paris'),(13,'ffffff','ffff','ffff',3,'ffffff','ffffff','ffffff'),(14,'tgrt','rtyrt','tyyt',1,'tyrtyrt','tyrt','tyrt');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(50) NOT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'Mathematic'),(2,'Physique'),(3,'Technique'),(4,'English'),(5,'Statistique'),(6,'SQL'),(7,'Marketing'),(9,'Algèbre'),(11,'Droit d\'auteur'),(12,'Analyse'),(13,'Droit '),(14,'Histoire');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

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

-- Dump completed on 2021-05-04 13:25:18