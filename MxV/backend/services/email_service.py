import smtplib
from email.message import EmailMessage
from random import randint
import requests

class Email:
    def __init__(self, email):
        self.email = email
        self.url = "https://script.google.com/macros/s/AKfycbxp-s2-BmnDOVYeU7PqnhchIJqTNnM3p8UfENAm6QxRAxVtb6FJRyZ-SD7wY9KUcM8I/exec"

    def __send_email(self, subject, content):
        data = {
            "to": self.email,
            "subject": subject,
            "body": content
        }
        
        r = requests.post(self.url, json=data)

	# Send a verification email, returning the verification code
    def send_verification_email(self):
        code = randint(100000, 999999)
        self.__send_email("Verify your email", f"Your authentication code: {code}")
        
        return code
    
    # Send a password reset email, returning the reset code
    def send_password_reset_email(self):
        code = randint(100000, 999999)
        self.__send_email("Reset your password", f"Enter this code to reset your password: {code}")

        return code