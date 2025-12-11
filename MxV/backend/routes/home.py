from flask import Blueprint, render_template
from services import Home

home_bp = Blueprint("home", __name__)

@home_bp.route("/home/<int:id>")
def home(id):
	# Get all the relevant data to be displayed
	service = Home(id)
	user_data = service.user_data()
	question_data = service.question_data()
	momentum_data = service.momentum_data()

	return render_template("home.html", user_data=user_data, question_data=question_data, momentum_data=momentum_data, id=id)