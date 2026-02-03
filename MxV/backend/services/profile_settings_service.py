from database import Select, Update

class ProfileSettingsService:
	def __init__(self, username, bio, id):
		self.new_username = username
		self.new_bio = bio
		self.id = id
		self.user_data = Select.get_user_data(id)
	
	# Commit the users profile changes to the database
	def commit_changes(self):
		old_username = self.user_data["username"]
		old_bio = self.user_data["bio"]
		if old_username == self.new_username and old_bio == self.new_bio:
			return 67
		
		# Change has been made
		Update.update_profile_data(self.id, self.new_username, self.new_bio)
