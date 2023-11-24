import jwt

SECRET = "ABCD123"

def encrypt(user_id,user_type):
    token = jwt.encode({"id":user_id,"type":user_type},SECRET,algorithm="HS256")
    return token