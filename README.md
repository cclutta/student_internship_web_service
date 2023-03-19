# Student Internship Web Service Project

### Introduction
This is a simple REST API that colleges can use to manage internships. Lecturers with internship opportunities can add them and encourage students to apply making the process of finding an internship less difficult for students.

### Web Service Features
* Students and lecturers can sign up and get accounts
* Users can be authenticated using username/password or tokens
* All users (especially students) can view available internships
* Lecturers can add internships directly and assign to specific students
* Students can apply and get approval for internships

### Installation Guide
* Clone the repo
* Install all dependencies in requirements.txt
* Set up database using setup_mysql_db.sql

### Usage
* Run the application using the following variables.

`SI_MYSQL_USER='si_user' SI_MYSQL_PWD='si_user_pwd' SI_MYSQL_HOST='localhost' SI_MYSQL_DB='student_internship' ./app.py`

### API Endpoints

#### Users
| HTTP Verbs | Endpoints | Action | Role
| --- | --- | --- | --- |
| POST | /api/v1/users/ | To add a new user account | ADMIN
| GET | /api/v1/users/ | To get all users | ADMIN
