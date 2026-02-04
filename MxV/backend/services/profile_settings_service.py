from database import Select, Update

class ProfileSettingsService:
	def __init__(self, username, bio, id):
		self.new_username = username
		self.new_bio = bio
		user_data = Select.get_user_data(id)
		self.id = id
		self.old_username = user_data["username"]
		self.old_bio = user_data["bio"]
	
	# Commit the users profile changes to the database
	def commit_changes(self):
		if self.old_username == self.new_username and self.old_bio == self.new_bio:
			return 67
		
		# Change has been made
		Update.update_profile_data(self.id, self.new_username, self.new_bio)
