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
| GET | /api/v1/users/<user_id> | Get specific user with user_id | ADMIN
| GET | /api/v1/users/token | Get token for authentication | USER

##### Sample

`GET /users/<user_id>`

    curl -i -u example@gmail.com:test123 0.0.0.0:5000/api/v1/users/7

Response:
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 19 Mar 2023 06:22:25 GMT
Content-Type: application/json
Content-Length: 214
Access-Control-Allow-Origin: *
Connection: close

{
  "created_on": null,
  "email": "name@gmail.com",
  "enabled": 0,
  "first_name": "John",
  "id": 7,
  "last_name": "Name",
  "phone": "756908765",
  "roles": [
    {
      "name": "LECTURER"
    }
  ]
}
```
#### Lecturers
| HTTP Verbs | Endpoints | Action | Role
| --- | --- | --- | --- |
| POST | /api/v1/lecturers/ | To add a new lecturer account | ADMIN
| GET | /api/v1/lecturers/ | To get all lecturers | ADMIN
| GET | /api/v1/lecturers/<lec_id> | Get specific lecturer with lec_id | ADMIN, LECTURER

##### Sample
`GET /lecturers`

     curl -i -u example@gmail.com:test123 0.0.0.0:5000/api/v1/lecturers
     
Response:
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 19 Mar 2023 06:33:54 GMT
Content-Type: application/json
Content-Length: 1453
Access-Control-Allow-Origin: *
Connection: close

[
  {
    "address": "here",
    "department": "HOIE8",
    "email": "mashabe@gmail.com",
    "first_name": "Masha",
    "gender": "F",
    "id": 1,
    "last_name": "Bear",
    "lecturer_id": "HKOOE",
    "phone": "93723202"
  },
  {
    "address": "Hollywood Lane",
    "department": "Music",
    "email": "jbj@gmail.com",
    "first_name": "Jon",
    "gender": "M",
    "id": 2,
    "last_name": "Bon",
    "lecturer_id": "M9023",
    "phone": "732909223"
  }
]
```
#### Students
| HTTP Verbs | Endpoints | Action | Role
| --- | --- | --- | --- |
| POST | /api/v1/students/ | To add a new student account | ADMIN
| GET | /api/v1/students/ | To get all students | ADMIN, LECTURER
| GET | /api/v1/students/<student_id> | Get specific student with student_id | ADMIN, LECTURER
| POST | /api/v1/students/approve_payment | Approve payments for students to access internships | ADMIN
| GET | /api/v1/students/approved | Get students who have paid for service | ADMIN, LECTURER

##### Sample
`GET /students/<student_id>`

    curl -i -u example@gmail.com:test123 0.0.0.0:5000/api/v1/students/2

Response:
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Mon, 20 Mar 2023 14:58:38 GMT
Content-Type: application/json
Content-Length: 291
Access-Control-Allow-Origin: *
Connection: close

{
  "address": "here",
  "course_code": "HOIE8",
  "email": "harry@gmail.com",
  "first_name": "Harry",
  "gender": "M",
  "id": 2,
  "kin_name": "James Holden",
  "kin_phone": "9732329428",
  "last_name": "Mayor",
  "payment_approved": 1,
  "phone": "9372343202",
  "student_id": "HKOOE"
}
```
#### Internships
| HTTP Verbs | Endpoints | Action | Role
| --- | --- | --- | --- |
| POST | /api/v1/internships/ | To add a new internship opportunity | LECTURER
| GET | /api/v1/internships/ | To get all internship opportunities | ADMIN, LECTURER, STUDENT
| GET | /api/v1/internships/<internship_id> | Get specific internship with internship_id | ADMIN, LECTURER, STUDENT
| POST | /api/v1/internships/apply | Apply for specific opportunity | STUDENT
| POST | /api/v1/internships/assign | Assign a student a specific opportunity | LECTURER
| GET | /api/v1/internships/assigned | Get all assigned opportunities | ADMIN, LECTURER, STUDENT
| GET | /api/v1/internships/added-by-me | Get all internships added by a specific lecturer | LECTURER

##### Sample
`GET /internships/assigned`

    curl -i -u example@gmail.com:test123 0.0.0.0:5000/api/v1/internships/assign -H 'Content-Type: application/json' -d '{"internship_id":"1", "student_id":"1"}'

Response:
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Mon, 20 Mar 2023 15:12:31 GMT
Content-Type: application/json
Content-Length: 57
Access-Control-Allow-Origin: *
Connection: close

{
  "Status": "Assignment successful"
}

```
### Authors
Chelsea Lutta (https://github.com/cclutta)









