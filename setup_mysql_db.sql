-- creates db for web service

CREATE DATABASE IF NOT EXISTS student_internship;
CREATE USER IF NOT EXISTS 'si_user'@'localhost' IDENTIFIED BY 'si_user_pwd';
GRANT ALL PRIVILEGES ON `student_internship`.* TO 'si_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'si_user'@'localhost';
FLUSH PRIVILEGES;

USE student_internship;

--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `enabled` tinyint(4) NOT NULL DEFAULT '0',
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;

CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50),
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`) 
);

--
-- Table structure for table `user_roles`
--
DROP TABLE IF EXISTS `user_roles`;

CREATE TABLE `user_roles` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  CONSTRAINT `FK_AUTH_01` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `FK_USER_01` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
);

INSERT INTO roles (name) VALUES ('ADMIN');
INSERT INTO roles (name) VALUES ('LECTURER');
INSERT INTO roles (name) VALUES ('STUDENT');

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `student_id` varchar(50) NOT NULL,
  `national_id` varchar(50) NOT NULL,
  `address` varchar(128) NOT NULL,
  `kin_name` varchar(50) NOT NULL,
  `kin_phone` varchar(50) NOT NULL,
  `payment_approved` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `lecturers`
--

DROP TABLE IF EXISTS `lecturers`;

CREATE TABLE `lecturers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `department` varchar(10) NOT NULL,
  `lecturer_id` varchar(50) NOT NULL,
  `national_id` varchar(50) NOT NULL,
  `address` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `internships`
--

DROP TABLE IF EXISTS `internships`;

CREATE TABLE `internships` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `job_summary` varchar(1024) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `period_months` int(11) DEFAULT '0',
  `renumeration_in_kes` varchar(255) DEFAULT '0',
  `start_date` date DEFAULT NULL,
  `added_on` date DEFAULT NULL,
  `lecturer_id` int(11) DEFAULT NULL,
  `assigned_student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
  );

--
-- Table structure for table `internship_applications`
--
DROP TABLE IF EXISTS `internship_applications`;

CREATE TABLE `internship_applications` (
  `student_id` int(11) NOT NULL,
  `internship_id` int(11) NOT NULL,
  CONSTRAINT `FK_STD_01` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `FK_INT_01` FOREIGN KEY (`internship_id`) REFERENCES `internships` (`id`)
);

