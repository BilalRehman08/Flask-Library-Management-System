from flask import Blueprint, request
from db import db
from controllers.users import add_customer as AddCustomer

add_customer_bp = Blueprint('add_customer','user_service')

@add_customer_bp.route('/register-customer',methods= ["POST"])
def add_customer_route():
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
    user_id = AddCustomer.add_customer_controller(db,email = data.get("email"),password = data.get("password"))
    return {
        "data":{
            "id": user_id
        }
    }, 200
    
    
def validate_data(data):
    error_msg = None
    if((data.get("email") is None) or len(data.get("email").strip())==0):
        error_msg = "Email field is required"
    if((data.get("password") is None) or len(data.get("password").strip())==0):
        error_msg = "Password field is required"
        
    return error_msg