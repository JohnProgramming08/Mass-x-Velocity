from .create_db import db, User


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
		found_user = User.query.filter(User.email == email and User.password_hash == password_hash).first()
		
		if found_user is None:
			return False
		
		return found_user.user_id
