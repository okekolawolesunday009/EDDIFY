-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: eddify_dev_db
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.20.04.1

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_name` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('HTML','109fa993-e149-4e02-ac34-77a1e75bebad','2024-02-25 17:40:47','2024-02-25 17:40:47'),('HTML','bee3dd73-e2d9-41a3-9c62-e86b47b9f1d3','2024-02-25 17:11:36','2024-02-25 17:11:36');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `category_id` varchar(60) NOT NULL,
  `title` varchar(128) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `number_lesson` int NOT NULL,
  `hours_lesson` int NOT NULL,
  `number_quiz` int NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('bee3dd73-e2d9-41a3-9c62-e86b47b9f1d3','HTML TAGS','Learn about HTML Tags',2,5,0,'5d0163ef-08ab-4baa-8c5e-8aa8065ae3c0','2024-02-25 17:11:36','2024-02-25 17:11:36'),('109fa993-e149-4e02-ac34-77a1e75bebad','Advance TAGS','Advance',4,2,0,'68e111db-dc2e-4054-a280-150ed7b96377','2024-02-25 17:40:47','2024-02-25 17:40:47'),('bee3dd73-e2d9-41a3-9c62-e86b47b9f1d3','Advance TAGS','Advance',4,2,0,'68ec83fe-9392-49f4-acf0-67c0c0dc8471','2024-02-25 17:11:36','2024-02-25 17:11:36'),('109fa993-e149-4e02-ac34-77a1e75bebad','HTML TAGS','Learn about HTML Tags',2,5,0,'b7bc227a-0676-470f-962c-cae77c8eb5aa','2024-02-25 17:40:47','2024-02-25 17:40:47');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollments`
--

DROP TABLE IF EXISTS `enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollments` (
  `course_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`),
  CONSTRAINT `enrollments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES ('5d0163ef-08ab-4baa-8c5e-8aa8065ae3c0','5436784e-cd85-425b-8b81-4d71b88e5230','1a5137a1-33c5-4a87-8736-29f91f46bbde','2024-02-25 17:11:36','2024-02-25 17:11:36'),('b7bc227a-0676-470f-962c-cae77c8eb5aa','732d7b1c-b071-47c7-887c-c542d48a9c76','818b1c82-8e8f-451c-b386-1a8a47d06d95','2024-02-25 17:40:47','2024-02-25 17:40:47');
/*!40000 ALTER TABLE `enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons`
--

DROP TABLE IF EXISTS `lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lessons` (
  `lesson_title` varchar(128) NOT NULL,
  `description` varchar(258) NOT NULL,
  `content` varchar(250) NOT NULL,
  `course_id` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `lessons_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons`
--

LOCK TABLES `lessons` WRITE;
/*!40000 ALTER TABLE `lessons` DISABLE KEYS */;
INSERT INTO `lessons` VALUES ('HTML5 TAGS','Html is a mark up language','ZhULGD5hNQs','5d0163ef-08ab-4baa-8c5e-8aa8065ae3c0','a021ea78-1570-42d8-8fb0-67c0c0fc5ad2','2024-02-25 17:11:36','2024-02-25 17:11:36'),('HTML5 TAGS','Html is a mark up language','ZhULGD5hNQs','b7bc227a-0676-470f-962c-cae77c8eb5aa','b0803158-4835-4175-b0dc-79b713f6b9dc','2024-02-25 17:40:47','2024-02-25 17:40:47');
/*!40000 ALTER TABLE `lessons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quizs`
--

DROP TABLE IF EXISTS `quizs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quizs` (
  `quiz_title` varchar(128) NOT NULL,
  `content` varchar(250) NOT NULL,
  `lesson_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`),
  CONSTRAINT `quizs_ibfk_1` FOREIGN KEY (`lesson_id`) REFERENCES `lessons` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quizs`
--

LOCK TABLES `quizs` WRITE;
/*!40000 ALTER TABLE `quizs` DISABLE KEYS */;
/*!40000 ALTER TABLE `quizs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `course_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `text` varchar(1024) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_course_association`
--

DROP TABLE IF EXISTS `user_course_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_course_association` (
  `UserID` varchar(60) DEFAULT NULL,
  `CourseID` varchar(60) DEFAULT NULL,
  KEY `UserID` (`UserID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `user_course_association_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`id`),
  CONSTRAINT `user_course_association_ibfk_2` FOREIGN KEY (`CourseID`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_course_association`
--

LOCK TABLES `user_course_association` WRITE;
/*!40000 ALTER TABLE `user_course_association` DISABLE KEYS */;
INSERT INTO `user_course_association` VALUES ('5436784e-cd85-425b-8b81-4d71b88e5230','5d0163ef-08ab-4baa-8c5e-8aa8065ae3c0'),('5436784e-cd85-425b-8b81-4d71b88e5230','68ec83fe-9392-49f4-acf0-67c0c0dc8471'),('732d7b1c-b071-47c7-887c-c542d48a9c76','b7bc227a-0676-470f-962c-cae77c8eb5aa'),('732d7b1c-b071-47c7-887c-c542d48a9c76','68e111db-dc2e-4054-a280-150ed7b96377');
/*!40000 ALTER TABLE `user_course_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone_no` varchar(128) NOT NULL,
  `image_file` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('','','','','','','0d3d4601-741c-4ffd-b060-c61ca1b3b496','2024-02-25 17:41:36','2024-02-25 17:41:36'),('','','','','','','0deb0b2b-380d-4bfe-a37b-c2bf6af6adfe','2024-02-25 17:49:46','2024-02-25 17:49:46'),('','','','','','','103cb99a-88f3-419b-8d65-8d5db60c1475','2024-02-25 17:53:08','2024-02-25 17:53:08'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','1be7785a-aeab-448a-b157-e74a4b68645c','2024-02-25 17:48:22','2024-02-25 17:48:22'),('adamu','james','admu@gmail.com','12345','123455','C:\\fakepath\\adun.jpg','2fe48580-5150-4e46-a214-529189d79f0e','2024-02-25 17:58:47','2024-02-25 17:58:47'),('','','','','','','340d73ee-5e90-403f-beeb-d64202fde8aa','2024-02-25 17:52:04','2024-02-25 17:52:04'),('','','','','','','4159cd1b-4a49-49f7-b050-da730724991d','2024-02-25 17:44:13','2024-02-25 17:44:13'),('','','','','','','49b765a9-6e70-4352-ac89-97692ffaac61','2024-02-25 17:54:39','2024-02-25 17:54:39'),('victor','Osimehn','admin@gmail.com','12345678','070000000','01','5436784e-cd85-425b-8b81-4d71b88e5230','2024-02-25 17:11:36','2024-02-25 17:11:36'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','65b35269-7adc-429a-9175-1a422c4c9ee9','2024-02-25 17:44:50','2024-02-25 17:44:50'),('','','','','','','703cf385-e454-4989-9ba7-2f88f1ff30d5','2024-02-25 17:52:25','2024-02-25 17:52:25'),('victor','Osimehn','admin@gmail.com','12345678','070000000','01','732d7b1c-b071-47c7-887c-c542d48a9c76','2024-02-25 17:40:47','2024-02-25 17:40:47'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','7a0a1716-319b-4e3c-bdf3-8adc7b57d742','2024-02-25 17:47:19','2024-02-25 17:47:19'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','886cade4-2c98-445e-8c67-24b5793a0ab0','2024-02-25 17:47:06','2024-02-25 17:47:06'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','8d2869ae-8c4d-405e-9fd1-4db6dd8cdd2e','2024-02-25 17:48:57','2024-02-25 17:48:57'),('','','','','','','8f4be2c0-8911-45bd-9b1f-205d7bbd36c8','2024-02-25 17:53:12','2024-02-25 17:53:12'),('','','','','','','ad6164b2-df64-4bd7-a5ec-465fdf8c7a5a','2024-02-25 17:53:54','2024-02-25 17:53:54'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','b859810d-d0ec-4d16-998f-c8f8c6b968d9','2024-02-25 17:47:35','2024-02-25 17:47:35'),('','','','','','','bef84210-f165-49be-b1df-208ceb4f78b4','2024-02-25 17:53:06','2024-02-25 17:53:06'),('','','','','','','ca15ab75-7abf-4381-9eaf-b824bad42441','2024-02-25 17:54:15','2024-02-25 17:54:15'),('','','','','','','cdb10343-3824-456d-90d0-d35da5157e1f','2024-02-25 17:54:41','2024-02-25 17:54:41'),('oke kolawol','sunday','ade@gmail.com','12345','12345','C:\\fakepath\\adun.jpg','d265d266-4de9-44d2-95bc-c8e5c554f094','2024-02-25 17:46:27','2024-02-25 17:46:27'),('','','','','','','d40abbda-4260-45fb-b244-448a6951ccf9','2024-02-25 17:53:39','2024-02-25 17:53:39'),('','','','','','','d40e1982-3074-467e-84a6-216334c2bae4','2024-02-25 17:53:45','2024-02-25 17:53:45'),('','','','','','','e3a3a91a-14ae-4f6f-8aaa-ff92b81faff6','2024-02-25 17:54:01','2024-02-25 17:54:01'),('','','','','','','fb306850-378e-48f5-98b7-e4b2be582b9d','2024-02-25 17:54:19','2024-02-25 17:54:19');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-27 16:30:29
