from flask import Blueprint, request
from db import db
from controllers.users import login_user as LoginController
from services import token_service

login_user_bp = Blueprint("login_user","user_service")

@login_user_bp.route("/login",methods = ["POST"])
def login_user_route():
    # Check request data type
    if not request.is_json:
        return {
            "error":{
                "message": "API accept JSON data"
            }
        }, 400
    
    # Data validation
    data = request.get_json()
    if(error:= validate_data(data)) is not None:
        return {
            "error":{
                "message": error
            }
        }
    user_id = LoginController.login_user_controller(db,email = data.get("email"),password = data.get("password"),user_type=data.get("user_type"))
    if (user_id!=None):
        return {
            "data":{
                "message": "User login Successful",
                "token": token_service.encrypt(user_id['id'],data.get('user_type'))
            }
        }, 200
    else:
        return{
            "error":{
                "message": "Invalid email or password"
            }
        }, 400
    
    
def validate_data(data):
    error_msg = None
    if((data.get("email") is None) or len(data.get("email").strip())==0):
        error_msg = "Email field is required"
    elif((data.get("password") is None) or len(data.get("password").strip())==0):
        error_msg = "Password field is required"
    elif((data.get("user_type") is None) or len(data.get("user_type").strip())==0):
        error_msg = "User type is required"
    
    return error_msg   
