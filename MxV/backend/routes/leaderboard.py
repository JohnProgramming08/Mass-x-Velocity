from flask import Blueprint, render_template, redirect, url_for, request, session
from services import Leaderboard

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("/leaderboard/<int:id>")
def settings(id):
    top_users = Leaderboard.get_top_users()
    return render_template("leaderboard.html", id=id, top_users=top_users)