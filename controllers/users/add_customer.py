from query.users import add_customer as AddCustomer

def add_customer_controller(db,email,password):
    conn = db.connect()
    user_id = AddCustomer.add_customer_query(conn,email,password)
    db.disconnect(conn)
    return user_id