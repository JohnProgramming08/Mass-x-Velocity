from flask import Blueprint, render_template, session, url_for
from services import Reset
from forms import ResetForm, ValidationForm

reset_bp = Blueprint("reset", __name__)


@reset_bp.route("/reset")
def reset():
	email_form = ResetForm()
	code_form = ValidationForm()
	if not email_form.validate_on_submit():
		return render_template("reset.html", email_form=email_form)
	
	# User has submitted the email form
	if email_form.validate_on_submit():
		email = email_form.email.data
		session["email"] = email
		service = Reset(email)
		service.send_email()
		return render_template("reset.hmtl", email_form=email_form, code_form=code_form)
	
	# User has submitted the code form
	if code_form.validate_on_submit():
		email = session["email"]
		service = Reset(email)
		code = code_form.code.data
		
		# Input validation code is correct
		if service.reset_password(code):
			return render_template(url_for("join.join"))
		
		return render_template("reset.html", email_form=email_form)
	