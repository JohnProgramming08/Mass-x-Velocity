from .create_db import db, User, Stats


class Select:
	# Return whether or not a user with the given email exists
	@staticmethod
	def email_exists(email):
		found_email = User.query.filter(User.email == email).first()
		if found_email is None:
			return 	False
		
		return True
		
	# Return the users id
	@staticmethod
	def get_id(email, password_hash):
		found_user = User.query.filter((User.email == email) & (User.password_hash == password_hash)).first()
		
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
			"exam2": user_stats.exam2_momentum
		}
	
	# Return the users accuracy and total number of answers given
	@staticmethod
	def get_answer_data(id):
		user_stats = Stats.query.filter(Stats.user_id == id).first()
		
		return {
			"total": user_stats.total_answers,
			"wrong": user_stats.wrong_answers
		}
	
	# Return general user data
	@staticmethod
	def get_user_data(id):
		user_stats = User.query.filter(User.user_id == id).first()
		
		return {
			"username": user_stats.username,
			"bio": user_stats.bio,
			"join_date": user_stats.join_date.strftime("%x")
		}
