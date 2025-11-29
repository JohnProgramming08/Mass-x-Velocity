import hashlib
from database import Select, Insert


class Join:
	def __init__(self, form):
		# Create user details
		self.password = form.password
		self.email = form.email
		self.username = self.email[0:5]
		self.bio = "Sorry, this feature is still in development!"
		
		# Possible errors and their messages
		self.errors = {
			"empty_password": "You must enter a password.",
			"has_space": "Your password must not have spaces.",
			"email_exists": "An account with this email already exists.",
			"incorrect": "Email or password is incorrect."
		}
	
	# Return the hashed password
	def hash(self):
		if self.password == "":
			return "empty_password"
		
		elif " " in self.password:
			return "has_space"
		
		full_hashed_password = int(hashlib.sha256(self.password.encode("utf-8")).hexdigest(), 16)
		self.password_hash = full_hashed_password % (10**8)

		return self.password_hash
	
	# Create a new user account and return the users id
	def signup(self):
		# Ensure email is not already taken
		found_user = Select.email_exists(self.email)
		if found_user:
			return self.error_message("email_exists")
		
		# Ensure password is correct
		self.password_hash = self.hash()
		if type(self.password_hash) is not int:
			return self.error_message(self.password_hash)
		
		# Successful
		id = Insert.insert_user(self.username, self.email, self.password_hash, self.bio)
		return id
	
	# Return the id of the user
	def login(self):
		# Ensure password is correct
		self.password_hash = self.hash()
		if type(self.password_hash) is not int:
			return self.error_message(self.password_hash)
		
		# Get id
		user_id = Select.get_id(self.email, self.password_hash)

		if user_id is None:
			return self.error_message("incorrect")
		else:
			return user_id
		
	# Return the appropriate error message
	def error_message(self, error):
		return self.errors[error]
	