from flask import Flask
from routes.users import users_router_list

app = Flask(__name__)

for route in users_router_list:
    app.register_blueprint(route)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )