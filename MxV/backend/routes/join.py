from flask import Blueprint, render_template, redirect, url_for
from forms import LogInForm, SignUpForm
from services import Join


join_bp = Blueprint("main", __name__)

@join_bp.route("/join/<clicked>", methods=["GET", "POST"])
def join(clicked):
	log_in_form = LogInForm()
	sign_up_form = SignUpForm()
	success = False

	# User has not submitted a form
	if not log_in_form.validate_on_submit() and not sign_up_form.validate_on_submit():
		return render_template("join.html", clicked=clicked, sign_up_form=sign_up_form, log_in_form=log_in_form, log_in_error="none", sign_up_error="none")
	
	# User is attempting to sign up
	if sign_up_form.validate_on_submit():
		logic = Join(sign_up_form)
		id = logic.signup()
		if type(id) is not int:
			return render_template("join.html", clicked=clicked, sign_up_form=sign_up_form, log_in_form=log_in_form, log_in_error="none", sign_up_error=id)
		
		# User has successfully signed up
		success = True
	
	# User is attempting to log in
	else:
		logic = Join(log_in_form)
		id = logic.login()
		if type(id) is not int:
			return render_template("join.html", clicked=clicked, sign_up_form=sign_up_form, log_in_form=log_in_form, log_in_error=id, sign_up_error="none")

		# User has successfully logged in
		success = True

	if success:
		return redirect(url_for("home"))