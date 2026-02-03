from flask import Blueprint, session, render_template, redirect, url_for
from forms import ProfileSettingsForm
from services import ProfileSettingsService

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/profile-settings/<int:id>", methods=["GET", "POST"])
def settings(id):
	form = ProfileSettingsForm

	if not form.validate_on_submit():
		return render_template("profile_settings.html", id=id, form=form)

	# User has submitted a form
	username = form.username
	bio = form.bio
	logic = ProfileSettingsService(username, bio, id)
	logic.commit_changes()
	
	return render_template("home.html", id=id)