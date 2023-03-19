#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Lecturers """
from models.lecturer import Lecturer
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.views.users import *
# from api.v1.views.internships import *


@app_views.route('/lecturers', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_lecturers():
    """
    Retrieves the list of all lecturer objects
    """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"})

    all_lecturers = storage.all(Lecturer)
    list_lecturers = []
    for lecturer in all_lecturers:
        lct = Lecturer.serialize(lecturer)
        list_lecturers.append(lct)
    return jsonify(list_lecturers)

@app_views.route('/lecturers/<lecturer_id>', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_lecturer(lecturer_id):
    """ Retrieves user using specific ID. """
    if not check_role("ADMIN") and not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"})

    lecturer = storage.get(Lecturer, lecturer_id)
    if not lecturer:
        abort(404)
    return jsonify(Lecturer.serialize(lecturer))

@app_views.route('/lecturers', methods=['POST'], strict_slashes=False)
@auth.login_required
def new_lecturer():
    """
    Adds a new lec
    """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"})

    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    gender = request.json.get('gender')
    email = request.json.get('email')    
    phone = request.json.get('phone')
    password = request.json.get('password')
    department = request.json.get('department')
    lecturer_id = request.json.get('lecturer_id')
    national_id = request.json.get('national_id')
    address = request.json.get('address')
    
   
    
    if first_name is None or last_name is None or email is None or phone is None or password is None or gender is None or department is None or lecturer_id is None or national_id is None or address is None:
        return ({"Error": "Missing Arguments"})
    
    if get_user_by_email(email) is not None:
        return ({"Error": "User Exists"})
        
    user = User(first_name=first_name, last_name=last_name, email=email, phone=phone)
    user.hash_password(password)
    user.roles.append(add_role('LECTURER'))
    
    lecturer = Lecturer(first_name=first_name, last_name=last_name, email=email, phone=phone, gender=gender, department=department, lecturer_id=lecturer_id, national_id=national_id, address=address)
    
    storage.new(user)
    storage.new(lecturer)
    storage.save()
    return jsonify({'username': user.email, 'Status':'Lecturer succesfully added'}), 201


def get_lec_by_email(email):
    """ Queries DB to find user with same mail. """
    lecs = storage.all(Lecturer)
    for lec in lecs:
        if lec.email == email:
            return lec
    return None
    
