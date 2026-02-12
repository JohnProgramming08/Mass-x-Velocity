from .email_service import Email
from database import Update, Select
from .hash_service import Hash

class Reset:
	def __init__(self, email):
		self.email = email
		self.id = Select.get_email_id(email)
		self.code = Select.get_code(self.id)
	
	# Send a password reset email to the user, saving the code sent
	def send_email(self):
		email_system = Email(self.email)
		code = email_system.send_password_reset_email()
		Update.update_code(self.id, code)
		
		return self.id

	# Reset the users password
	def reset_password(self, input_code):
		print("----------------CODE------------")
		print(self.code)
		print(int(input_code))
		# User input wrong code
		if self.code != int(input_code):
			return False
		
		# User input correct code
		hashed_password = Hash.hash_password("BlackButler")
		Update.update_password(self.id, hashed_password)
		return True
