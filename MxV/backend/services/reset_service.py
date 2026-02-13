from .email_service import Email
from database import Update, Select
from .hash_service import Hash

class Reset:
	def __init__(self, email, password, confirm_password):
		self.email = email
		self.password = password
		self.confirm_password = confirm_password
		self.id = Select.get_email_id(email)
		self.code = Select.get_code(self.id)

	# Ensure the password and confirm_password match
	def passwords_match(self):
		if self.password == self.confirm_password:
			return True
		
		return "Your entered passwords do not match."
	
	# Send a password reset email to the user, saving the code sent
	def send_email(self):
		email_system = Email(self.email)
		code = email_system.send_password_reset_email()
		Update.update_code(self.id, code)
		hashed_password = Hash.hash_password(self.password)
		Update.update_temporary_password(self.id, hashed_password)

		return self.id

	# Reset the users password
	def reset_password(self, input_code):
		# User input wrong code
		if self.code != int(input_code):
			return False
		
		# User input correct code
		hashed_password = Select.get_temporary_password(self.id)
		Update.update_password(self.id, hashed_password)
		return True
