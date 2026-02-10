from database import Select, Update
import os
from werkzeug.utils import secure_filename
import uuid

class ProfileSettingsService:
	def __init__(self, username, bio, image, id):
		self.new_username = username
		self.new_bio = bio
		self.image = image
		user_data = Select.get_user_data(id)
		self.id = id
		self.old_username = user_data["username"]
		self.old_bio = user_data["bio"]
	
	# Commit the users profile changes to the database
	def commit_changes(self):
		Update.update_profile_data(self.id, self.new_username, self.new_bio)
		self.process_image()

	# Update the users profile picture
	def process_image(self):
		if self.image is None:
			return 67
		
		# User has uploaded an image
		ext = os.path.splitext(self.image.filename)[1]
		filename = secure_filename(f"{uuid.uuid4()}{ext}")
		path = os.path.join("static/images/profile_pictures/", filename)
		self.image.save(path)
		
		# Delete the old profile picture and store the path of the new one
		old_path = Select.get_profile_picture(self.id)
		if path != "keating_pfp.png": # Default profile picture
			os.remove(f"static/images/profile_pictures/{old_path}")
		Update.update_profile_picture(self.id, filename)
