import hashlib
from database import Select, Insert, Update
from random import randint
from .email_service import Email
from .hash_service import Hash

class Join:
    def __init__(self, form):
        # Create user details
        self.password = form.password.data
        try:
            self.confirm_password = form.confirm_password.data
        except:
            pass
        self.email = form.email.data
        self.username = self.email[0:5]
        self.bio = "Sorry, this feature is still in development!"

        # Possible errors and their messages
        self.errors = {
            "empty_password": "You must enter a password.",
            "has_space": "Your password must not have spaces.",
            "email_exists": "An account with this email already exists.",
            "incorrect": "Email or password is incorrect.",
            "dont_match": "Your passwords don't match.",
            "unverified": "This account is unverified."
        }

    # Return the hashed password
    def hash(self):
        self.password_hash = Hash.hash_password(self.password)
        return self.password_hash

    # Create a new user account and return the users id
    def signup_verification(self):
        # Ensure email is not already taken
        found_user = Select.email_exists(self.email)
        if found_user is not None and found_user.verified:
            return self.error_message("email_exists")
        
        # Ensure password is correct
        self.password_hash = self.hash()
        if type(self.password_hash) is not int:
            return self.error_message(self.password_hash)
        if self.password != self.confirm_password:
            return self.error_message("dont_match")
        
		# Ensure that the email actually exists
        email_system = Email(self.email)
        code = email_system.send_verification_email()
        id = self.store_unverified_account(found_user, code)
        
        return id

    # Return the id of the user
    def login(self):
        # Ensure password is correct
        self.password_hash = self.hash()
        if type(self.password_hash) is not int:
            return self.error_message(self.password_hash)

        # Get id and verification status
        user_id = Select.get_id(self.email, self.password_hash)
        verified = Select.is_verified(self.password_hash, self.email)

        if user_id is False:
            return self.error_message("incorrect")
        elif verified is False:
            return self.error_message("unverified")
        else:
            return user_id

    # Return the appropriate error message
    def error_message(self, error):
        return self.errors[error]
    
    # Store an unverified account
    def store_unverified_account(self, user, code):
        if user is None:
            id = Insert.insert_user(self.username, self.email, self.password_hash, self.bio, code)

        else:
            Update.update_password(user.user_id, self.password_hash)
            Update.update_code(user.user_id, code)
            id = user.user_id
        return id
    
    # Verify the users email
    @staticmethod
    def verify(id, code):
        correct_code = Select.get_code(id)
        if int(code.data) == correct_code:
            Update.update_verified(id)
            return True
        return False
