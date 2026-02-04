from flask import Blueprint, render_template, redirect, url_for
from forms import ProfileSettingsForm
from services import ProfileSettingsService

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/profile-settings/<int:id>", methods=["GET", "POST"])
def settings(id):
	form = ProfileSettingsForm()

	if not form.validate_on_submit():
		logic = ProfileSettingsService("", "", id)
		bio = logic.old_bio
		username = logic.old_username
		return render_template("profile_settings.html", id=id, form=form, bio=bio, user_name=username)

	# User has submitted a form
	username = form.username.data
	bio = form.bio.data
	logic = ProfileSettingsService(username, bio, id)
	logic.commit_changes()
	
	return redirect(url_for("home.home", id=id))