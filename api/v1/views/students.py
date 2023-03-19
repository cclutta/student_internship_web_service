#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Students """
from models.student import Student
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.views.users import *


@app_views.route('/students', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_students():
    """
    Retrieves the list of all student objects
    """
    if not check_role("ADMIN") and not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"}) 
    
    all_students = storage.all(Student)
    list_students = []
    for student in all_students:
        std = Student.serialize(student)
        list_students.append(std)
    return jsonify(list_students)

@app_views.route('/students/<student_id>', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_student(student_id):
    """ Retrieves user using specific ID. """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"}) 
    
    student = storage.get(Student, student_id)
    if not student:
        abort(404)
    return jsonify(Student.serialize(student))

@app_views.route('/students', methods=['POST'], strict_slashes=False)
@auth.login_required
def new_student():
    """
    Adds a new student
    """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"}) 
    
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    gender = request.json.get('gender')
    email = request.json.get('email')    
    phone = request.json.get('phone')
    password = request.json.get('password')
    course_code = request.json.get('course_code')
    student_id = request.json.get('student_id')
    national_id = request.json.get('national_id')
    address = request.json.get('address')
    kin_name = request.json.get('kin_name')
    kin_phone = request.json.get('kin_phone')
    
    if first_name is None or last_name is None or email is None or phone is None or password is None or gender is None or course_code is None or student_id is None or national_id is None or address is None or kin_name is None or kin_phone is None:
        return ({"Error": "Missing Arguments"})
    
    if get_user_by_email(email) is not None:
        return ({"Error": "User Exists"})
        
    user = User(first_name=first_name, last_name=last_name, email=email, phone=phone)
    user.hash_password(password)
    user.roles.append(add_role('STUDENT'))
    
    student = Student(first_name=first_name, last_name=last_name, email=email, phone=phone, gender=gender, course_code=course_code, student_id=student_id, national_id=national_id, address=address, kin_name=kin_name, kin_phone=kin_phone)
    
    storage.new(user)
    storage.new(student)
    storage.save()
    return jsonify({'username': user.email, 'Status':'Student succesfully added'}), 201

@app_views.route('/students/approve_payment', methods=['POST'], strict_slashes=False)
@auth.login_required
def approve_payment():
    """
    Approve payment
    """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"})
    
    student_id = request.json.get('student_id')
    
    student = storage.get(Student, student_id)
    if not student:
        return ({"Error": "No Student found"})
    student.payment_approved = 1;
    storage.save()
    return jsonify({"Status": "Payment Approved"})

@app_views.route('/students/approved', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_approved_students():
    """
    Retrieves the list of all student objects paid
    """
    if not check_role("ADMIN") and not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"}) 
    
    all_students = storage.all(Student)
    list_students = []
    for student in all_students:
        if student.payment_approved == 1:
            std = Student.serialize(student)
            list_students.append(std)
    return jsonify(list_students)

def get_student_by_email(email):
    """ Queries DB to find user with same mail. """
    students = storage.all(Student)
    for std in students:
        if std.email == email:
            return std
    return None


    
