from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Create users table
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password_hash = db.Column(db.Integer)
    bio = db.Column(db.String(200), nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.now)
    verified = db.Column(db.Boolean, default=False)
    code = db.Column(db.Integer, nullable=False)
    profile_picture = db.Column(db.String(255), default="keating_pfp.png")
    temporary_password_hash = db.Column(db.Integer, default=67)

    # Related tables
    stats = db.relationship(
        "Stats", uselist=False, back_populates="user", cascade="all, delete-orphan"
    )


# Create stats table (composite relationship with users)
class Stats(db.Model):
    __tablename__ = "stats"
    total_answers = db.Column(db.Integer, default=0)
    wrong_answers = db.Column(db.Integer, default=0)
    total_momentum = db.Column(db.Integer, default=0)
    practice1_momentum = db.Column(db.Integer, default=0)
    practice2_momentum = db.Column(db.Integer, default=0)
    practice3_momentum = db.Column(db.Integer, default=0)
    exam1_momentum = db.Column(db.Integer, default=0)
    exam2_momentum = db.Column(db.Integer, default=0)

    # Related tables
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key=True)
    user = db.relationship("User", back_populates="stats")


# Create questions table (composite relationship with topic_questions)
# Filename of image is stored instead of the image itself
class Question(db.Model):
    __tablename__ = "questions"
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False, unique=True)
    question_image_filename = db.Column(db.String(255), default="None")
    answer = db.Column(db.Float, nullable=False)
    answer_units = db.Column(db.String(10), default="None")
    working_image_filename = db.Column(db.String(255), nullable=False, unique=True)
    level = db.Column(db.String(4), nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)

    # Related tables
    topic_questions = db.relationship(
        "TopicQuestion", back_populates="question", cascade="all, delete-orphan"
    )


# Create topic_questions table
class TopicQuestion(db.Model):
    __tablename__ = "topic_question"
    topic = db.Column(db.String(100), primary_key=True)

    # Related tables
    question_id = db.Column(
        db.Integer, db.ForeignKey("questions.question_id"), primary_key=True
    )
    question = db.relationship("Question", back_populates="topic_questions")
