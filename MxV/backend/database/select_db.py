from .create_db import db, User, Stats, TopicQuestion, Question


class Select:
    # Return whether or not a user with the given email exists
    @staticmethod
    def email_exists(email):
        return User.query.filter(User.email == email).first()

    # Return the users id
    @staticmethod
    def get_id(email, password_hash):
        found_user = User.query.filter(
            (User.email == email) & (User.password_hash == password_hash)
        ).first()

        if found_user is None:
            return False

        return found_user.user_id

    # Return all the users momentum data
    @staticmethod
    def get_all_momentum(id):
        user_stats = Stats.query.filter(Stats.user_id == id).first()

        return {
            "total": user_stats.total_momentum,
            "practice1": user_stats.practice1_momentum,
            "practice2": user_stats.practice2_momentum,
            "practice3": user_stats.practice3_momentum,
            "exam1": user_stats.exam1_momentum,
            "exam2": user_stats.exam2_momentum,
        }

    # Return the users accuracy and total number of answers given
    @staticmethod
    def get_answer_data(id):
        user_stats = Stats.query.filter(Stats.user_id == id).first()

        return {"total": user_stats.total_answers, "wrong": user_stats.wrong_answers}

    # Return general user data
    @staticmethod
    def get_user_data(id):
        user_stats = User.query.filter(User.user_id == id).first()

        return {
            "username": user_stats.username,
            "bio": user_stats.bio,
            "join_date": user_stats.join_date.strftime("%x"),
        }

    # Return a list of questions filtered by topic
    @staticmethod
    def get_topic_questions(topics_list, difficulties):
        question_id_list = []
        for topic in topics_list:
            questions = TopicQuestion.query.filter(TopicQuestion.topic == topic).all()

            # Some questions may have multiple topics
            for question in questions:
                difficulty = question.question.difficulty
                id = question.question_id

                if id not in question_id_list and difficulty in difficulties:
                    question_id_list.append(id)

        return question_id_list

    # Return an array of questions given their id's
    @staticmethod
    def get_questions(id_list):
        questions = []
        for id in id_list:
            question = Question.query.filter(Question.question_id == id).first()
            questions.append(question)

        return questions
    
	# Return the users authentication code
    @staticmethod
    def get_code(id):
        user = User.query.filter(id == User.user_id).first()
        return user.code
    
	# Return whether or not the user is verified
    @staticmethod
    def is_verified(password_hash, email):
        found_user = User.query.filter(
            (User.email == email) & (User.password_hash == password_hash)
        ).first()
        if found_user is not None:
            return found_user.verified
        else:
            return False
