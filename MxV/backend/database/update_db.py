from .create_db import db, Question, Stats, User


class Update:
    # Update user profile data
    @staticmethod
    def update_profile_data(user_id, username, bio):
        user_data = User.query.filter(User.user_id == user_id).first()
        user_data.username = username
        user_data.bio = bio
        db.session.commit()

    # Update users data for incorrect answer
    @staticmethod
    def update_incorrect_answer(user_id):
        user_stats = Stats.query.filter(Stats.user_id == user_id).first()
        user_stats.total_answers += 1
        user_stats.wrong_answers += 1
        db.session.commit()

    # Update users data for correct answer
    @staticmethod
    def update_correct_answer(user_id, momentum, difficulty):
        user_stats = Stats.query.filter(Stats.user_id == user_id).first()
        user_stats.total_answers += 1
        user_stats.total_momentum += momentum

        match difficulty:
            case "practice1":
                user_stats.practice1_momentum += momentum
            case "practice2":
                user_stats.practice2_momentum += momentum
            case "practice3":
                user_stats.practice3_momentum += momentum
            case "exam1":
                user_stats.exam1_momentum += momentum
            case "exam2":
                user_stats.exam2_momentum += momentum

        db.session.commit()
