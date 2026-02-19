from flask import Flask

from routes import register_routes
import database

# Initial setup
app = Flask(__name__)
app.secret_key = "SHHH"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1000 * 1000
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
database.db.init_app(app)

with app.app_context():
    try:
        database.db.create_all()
        database.Populate.populate_questions()
    except:
        pass
    


register_routes(app)


if __name__ == "__main__":
    app.run(debug=True, port=10000)
