import smtplib
from email.message import EmailMessage
from random import randint

class EmailService:
	# Send an email verification to given email, returning the verification code
    @staticmethod
    def send_verification_email(email):
        code = randint(100000, 999999)
        
        msg = EmailMessage()
        msg["Subject"] = "Verify your email"
        msg["From"] = "mxv.auth@gmail.com"
        msg["To"] = email
        msg.set_content(f"Your authentication code: {code}")
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("mxv.auth@gmail.com", "haqk hvje taix neux")
            smtp.send_message(msg)
        
        return code