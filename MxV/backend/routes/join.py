from flask import Blueprint, render_template, redirect, url_for, request, session
from forms import LogInForm, SignUpForm, ValidationForm
from services import Join


join_bp = Blueprint("join", __name__)


@join_bp.route("/join/<clicked>", methods=["GET", "POST"])
def join(clicked):
    log_in_form = LogInForm()
    sign_up_form = SignUpForm()
    validation_form = ValidationForm()
    success = False

    # User has not submitted a form
    if not log_in_form.validate_on_submit() and not sign_up_form.validate_on_submit() and not validation_form.validate_on_submit():
        return render_template(
            "join.html",
            clicked=clicked,
            sign_up_form=sign_up_form,
            log_in_form=log_in_form,
            log_in_error="",
            sign_up_error="",
        )

    # User is attempting to sign up
    if "sign_up" in request.form and sign_up_form.validate_on_submit():
        logic = Join(sign_up_form)
        id = logic.signup_verification()
        if type(id) is not int:
            return render_template(
                "join.html",
                clicked=clicked,
                sign_up_form=sign_up_form,
                log_in_form=log_in_form,
                log_in_error="",
                sign_up_error=id,
            )

        # Authentication email has been sent
        session["id"] = id
        return render_template(
            "join.html",
            clicked=clicked,
            sign_up_form=sign_up_form,
            log_in_form=log_in_form,
            log_in_error="",
            sign_up_error="",
            validation=True,
            validation_form = validation_form
		)
        

    # User is attempting to log in
    elif log_in_form.validate_on_submit():
        logic = Join(log_in_form)
        id = logic.login()
        if type(id) is not int:
            return render_template(
                "join.html",
                clicked=clicked,
                sign_up_form=sign_up_form,
                log_in_form=log_in_form,
                log_in_error=id,
                sign_up_error="",
            )

        # User has successfully logged in
        success = True

    # User is attempting to verify their email
    else:
        code = validation_form.code
        id=session["id"]
        correct_code = Join.verify(id, code)
        
        if correct_code:
            success = True
        else:
            return render_template(
                "join.html",
                clicked=clicked,
                sign_up_form=sign_up_form,
                log_in_form=log_in_form,
                log_in_error="",
                sign_up_error="NOOOOOOOO validation code wrong",
                validation=True,
                validation_form = validation_form
            )

    

    if success:
        return redirect(url_for("home.home", id=id))
