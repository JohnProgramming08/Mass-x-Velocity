import smtplib
from email.message import EmailMessage
from random import randint

class Email:
    def __init__(self, email):
        self.email = email

    def __send_email(self, subject, content):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = "mxv.auth@gmail.com"
        msg["To"] = self.email
        msg.set_content(content)
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("mxv.auth@gmail.com", "haqk hvje taix neux")
            smtp.send_message(msg)

	# Send a verification email, returning the verification code
    def send_verification_email(self):
        code = randint(100000, 999999)
        self.__send_email("Verify your email", f"Your authentication code: {code}")
        
        return code
    
    # Send a password reset email, returning the reset code
    def send_password_reset_email(self):
        code = randint(100000, 999999)
        self.__send_email("Reset your password", f"Enter this code to reset your password to 'BlackButler': {code}")

        return code