from flask import Blueprint, session, render_template, redirect, url_for
from forms import StudyForm
from services import Study

study_bp = Blueprint("study", __name__)

@study_bp.route("/study/<int:id>", methods=["GET", "POST"])
def study(id):
	form = StudyForm()
	questions = session.get("questions", [])
	question_logic = Study(questions, id)

	# User has not submitted a form
	if not form.validate_on_submit():
		question = question_logic.get_next_question()
		session["questions"] = question_logic.queue.data
		return render_template("study.html", question=question, correct="", form=form)
	
	answer = form.answer.data
	units = form.units.data
	correct = question_logic.submit_answer(units, answer)

	if correct:
		return render_template("study.html", question=question, correct="correct", form=form)
	
	return render_template("study.html", question=question, correct="incorrect", form=form)
