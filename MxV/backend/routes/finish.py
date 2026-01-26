from flask import Blueprint, render_template, session

finish_bp = Blueprint("finish", __name__)

@finish_bp.route("/finish/<int:id>")
def finish(id):
	correct = session["correct"]
	total = session["question_number"]
	accuracy = int(100 * (correct / total))
	gained_momentum = session["gained_momentum"]

	return render_template("finish.html", id=id, total=total, accuracy=accuracy, gained_momentum=gained_momentum)
