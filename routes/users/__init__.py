from routes.users.add_customer import add_customer_bp
from routes.users.login_user import login_user_bp

users_router_list = []
users_router_list.append(add_customer_bp)
users_router_list.append(login_user_bp)