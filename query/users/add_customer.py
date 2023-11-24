def add_customer_query(db_conn, email, password):
    query = """
        INSERT INTO user (email, password, user_type)
        VALUES (%(email)s,%(password)s,'CUSTOMER')
    """
    cur = db_conn.cursor()
    cur.execute(
        query, 
        {
            "email": email,
            "password":password,
        }
    )
    db_conn.commit()
    return cur.lastrowid
