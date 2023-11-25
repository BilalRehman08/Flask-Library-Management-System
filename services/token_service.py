import jwt
from flask import request

SECRET = "ABCD123"

def token_required(func):
    def _token_required(*args, **kwargs):
        decoded_data = None
        try:
            token = request.args.get("token")
            if token is None: raise Exception
            decoded_data = jwt.decode(token, SECRET, algorithms="HS256")
        except:
            return {"error": {"message": "Unauthenticated user"}}
        print(decoded_data)
        return func(decoded_data, *args, **kwargs)
    _token_required.__name__ = func.__name__
    return _token_required

def encrypt(user_id,user_type):
    token = jwt.encode({"id":user_id,"type":user_type},SECRET,algorithm="HS256")
    return token