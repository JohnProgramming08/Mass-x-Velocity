from flask import Blueprint, render_template, redirect, url_for, session
from forms import GCSETopicsForm, DifficultyForm
from services import Topics

topics_bp = Blueprint("topics", __name__)


@topics_bp.route("/topics/<int:id>", methods=["GET", "POST"])
def topics(id):
    gcse_form = GCSETopicsForm()
    difficulty_form = DifficultyForm()

    # If user has not submitted a form
    if not gcse_form.validate_on_submit():
        return render_template(
            "topics.html",
            id=id,
            gcse_form=gcse_form,
            difficulty_form=difficulty_form,
            error="",
        )

    # User has submitted a form
    logic = Topics(gcse_form, difficulty_form)
    valid = logic.check_valid()

    # Invalid form submition
    if valid["result"] == False:
        return render_template(
            "topics.html",
            id=id,
            gcse_form=gcse_form,
            difficulty_form=difficulty_form,
            error=valid["error"],
        )

    question_ids = logic.get_questions()
    session["question_number"] = 0
    session["last_id"] = 0
    session["correct"] = 0
    session["gained_momentum"] = 0
    session["next"] = False
    session["question_ids"] = question_ids  # Fetched in study.py
    return redirect(url_for("study.study", id=id))
