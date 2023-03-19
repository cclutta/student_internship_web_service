#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models.role import Role
from models import storage
from api.v1.views import app_views, auth
from flask import abort, jsonify, make_response, request, g


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"}) 
  
    all_users = storage.all(User)
    list_users = []
    for user in all_users:
        user = User.serialize(user)
        list_users.append(user)
    return jsonify(list_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_user(user_id):
    """ Retrieves user using specific ID. """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"})

    user = storage.get(User, user_id)
    if not user:
        return ({"Error":"No User Found"})
    return jsonify(User.serialize(user))

@app_views.route('/users', methods=['POST'], strict_slashes=False)
@auth.login_required
def new_user():
    """ Creates a new user. """
    if not check_role("ADMIN"):
        return ({"Error": "Action Not Permitted"}) 
        
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')    
    phone = request.json.get('phone')
    password = request.json.get('password')
    
    if first_name is None or last_name is None or email is None or phone is None or password is None:
        return ({"Error": "Missing Arguments"})

    if get_user_by_email(email) is not None:
        return ({"Error": "User Exists"})
    
    user = User(first_name=first_name, last_name=last_name, email=email, phone=phone)
    user.hash_password(password)
    storage.new(user)
    storage.save()
    return jsonify({'username': user.email}), 201

@app_views.route('/users/token', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })

def get_user_by_email(email):
    """ Queries DB to find user with same mail. """
    users = storage.all(User)
    for user in users:
        if user.email == email:
            return user
    return None

@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = get_user_by_email(email_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

def add_role(name):
    """ func to add role to user. """
    roles = storage.all(Role)
    for role in roles:
        if name == role.name:
            return role
    return None

def check_role(name):
    """ func to check logged in user role. """
    print(name in get_roles(g.user))
    return name in get_roles(g.user)

def get_roles(user):
    """ Func to get all roles. """
    list_roles = []
    for role in user.roles:
        list_roles.append(role.name)
    return list_roles
    
        
        
    

