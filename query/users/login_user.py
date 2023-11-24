def login_user_query(db_conn, email, password,user_type):
    query = """
        SELECT id FROM user where email=(%(email)s) AND password=(%(password)s) AND user_type=(%(user_type)s)
    """
    cur = db_conn.cursor()
    cur.execute(
        query, 
        {
            "email": email,
            "password":password,
            "user_type":user_type,
        }
    )
    db_conn.commit()
    return cur.fetchone()
