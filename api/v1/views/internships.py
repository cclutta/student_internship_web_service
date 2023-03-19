#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Internships """
from models.internship import Internship
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.views.users import *
from api.v1.views.students import *
from api.v1.views.lecturers import *


@app_views.route('/internships', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_internships():
    """
    Retrieves the list of all internship objects
    """
    all_internships = storage.all(Internship)
    list_internships = []
    for internship in all_internships:
        intp = Internship.serialize(internship)
        list_internships.append(intp)
    return jsonify(list_internships)

@app_views.route('/internships/<internship_id>', methods=['GET'], strict_slashes=False)
def get_internship(internship_id):
    """ Retrieves internship using specific ID. """
    internship = storage.get(Internship, internship_id)
    if not internship:
        return ({"Error": "No internship ID found"})
    return jsonify(Internship.serialize(internship))

@app_views.route('/internships', methods=['POST'], strict_slashes=False)
@auth.login_required
def new_internship():
    """
    Adds a new internship
    """
    if not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"})        
    
    title = request.json.get('title')
    company_name = request.json.get('company_name')
    industry = request.json.get('industry')
    job_summary = request.json.get('job_summary')    
    location = request.json.get('location')
    period_months = request.json.get('period_months')
    renumeration_in_kes = request.json.get('renumeration_in_kes')
    start_date = request.json.get('start_date')
    
    lecturer_id = get_lec_by_email(g.user.email).id
    
    if title is None or company_name is None or industry is None or job_summary is None or location is None or period_months is None or renumeration_in_kes is None or start_date is None:
        return ({"Error": "Missing Arguments"})
    
    internship = Internship(title=title, company_name=company_name, industry=industry, job_summary=job_summary, location=location, period_months=period_months, renumeration_in_kes=renumeration_in_kes, start_date=start_date, lecturer_id=lecturer_id)
        
    storage.new(internship)
    storage.save()
    return jsonify({'internship_id': internship.id, 'Status':'Internship succesfully added'}), 201
    
@app_views.route('/internships/apply', methods=['POST'], strict_slashes=False)
@auth.login_required
def apply_internship():
    """ Apply for internship. """
    if not check_role("STUDENT"):
        return ({"Error": "Action Not Permitted"})
    
    internship_id = request.json.get('internship_id')
        
    student = get_student_by_email(g.user.email)
    
    if student.payment_approved == 0:
        print(student.payment_approved)
        return ({"Error": "Service Unavailable. Payment not approved"})
    
    internship = storage.get(Internship, internship_id)
    if not internship:
        return ({"Error": "No internship ID found"})
        
    if internship.assigned_student_id is not None:
        return ({"Error": "Internship already assigned"})

    student.internship_applications.append(internship)
    storage.save()
   
    return jsonify({"Status": "Application successful"})
        
@app_views.route('/internships/assign', methods=['POST'], strict_slashes=False)
@auth.login_required
def assign_internship():
    """ Assign an internship. """
    if not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"})
        
    internship_id = request.json.get('internship_id')
    student_id = request.json.get('student_id')
    
    internship = storage.get(Internship, internship_id)
    student = storage.get(Student, student_id)
    
    if not internship or not student:
        return ({"Error": "Either Student or Internship ID not found"})
    
    internship.assigned_student_id = student_id
    storage.save()
    return jsonify({"Status": "Assignment successful"})

@app_views.route('/internships/assigned', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_assigned_internships():
    """
    Retrieves the list of all internship assigned
    """
    all_internships = storage.all(Internship)
    list_internships = []
    for internship in all_internships:
        if internship.assigned_student_id is not None:
            intp = Internship.serialize(internship)
            list_internships.append(intp)
    return jsonify(list_internships)
    
@app_views.route('/internships/added-by-me', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_internships_added():
    """
    Retrieves the list of all internships added by me
    """
    if not check_role("LECTURER"):
        return ({"Error": "Action Not Permitted"})
    
    lecturer = get_lec_by_email(g.user.email)
        
    all_internships = storage.all(Internship)
    list_internships = []
    for internship in all_internships:
        if internship.lecturer_id == lecturer.id:
            intp = Internship.serialize(internship)
            list_internships.append(intp)
    return jsonify(list_internships)
    
    
        
        
    
