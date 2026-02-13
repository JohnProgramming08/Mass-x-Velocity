from flask import Blueprint, render_template, session, url_for, redirect
from services import Reset
from forms import ResetForm, ValidationForm

reset_bp = Blueprint("reset", __name__)


@reset_bp.route("/reset", methods=["GET", "POST"])
def reset():
	email_form = ResetForm()
	code_form = ValidationForm()
	if not email_form.validate_on_submit() and not code_form.validate_on_submit():
		return render_template("reset.html", email_form=email_form)
	
	# User has submitted the code form
	if code_form.validate_on_submit():
		email = session["email"]
		service = Reset(email, "", "")
		code = code_form.code.data
		valid_code = service.reset_password(code)

		# Input validation code is correct
		if valid_code:
			return redirect(url_for("join.join", clicked="login"))
		
		return render_template("reset.html", email_form=email_form)

	# User has submitted the email form
	if email_form.validate_on_submit():
		# Get form data
		email = email_form.email.data
		password = email_form.new_password.data
		confirm_password = email_form.confirm_password.data

		session["email"] = email
		service = Reset(email, password, confirm_password)
		# Passwords match
		match = service.passwords_match()
		if match is True:
			service.send_email()
			return render_template("reset.html", email_form=email_form, code_form=code_form, code_sent=True)
		
		# Passwords don't match
		return render_template("reset.html", email_form=email_form, error=match)