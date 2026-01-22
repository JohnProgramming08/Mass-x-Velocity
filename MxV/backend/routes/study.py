from flask import Blueprint, session, render_template, redirect, url_for
from forms import StudyForm
from services import Study

study_bp = Blueprint("study", __name__)

@study_bp.route("/study/<int:id>", methods=["GET", "POST"])
def study(id):
	form = StudyForm()
	question_ids = session.get("question_ids", [])
	question_logic = Study(question_ids, id)

	question_number = session["question_number"]

	# User has not submitted a form
	if not form.validate_on_submit():
		question_number += 1
		session["question_number"] = question_number
		question = question_logic.get_next_question()
		session["question_ids"] = question_logic.queue.data
		return render_template("study.html", question=question, correct="", form=form, id=id, question_number=question_number, momentum=-1)
	
	question = question_logic.get_current_question()
	answer = form.answer.data
	units = form.units.data
	correct = question_logic.submit_answer(units, answer)

	if correct > 0:
		return render_template("study.html", question=question, correct="correct", form=form, id=id, question_number=question_number, momentum=correct)
	
	return render_template("study.html", question=question, correct="incorrect", form=form, id=id, question_number=question_number, momentum=0)


