from flask import Flask

from routes import register_routes
import database

# Initial setup
app = Flask(__name__)
app.secret_key = "SHHH"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
database.db.init_app(app)

with app.app_context():
	database.db.create_all()

register_routes(app)

if __name__ == "__main__":
	app.run(debug=True)