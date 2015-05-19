from email_settings import EMAIL, EMAIL_PASSWORD
import smtplib
from email.mime.text import MIMEText


class EmailSender:

    @staticmethod
    def send_email(email_receiver, message_text):
        message = MIMEText(message_text)
        message["Subject"] = "Reset Password Programming 101 v3 Week9 Task"
        message["To"] = email_receiver
        message["From"] = EMAIL
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(message)
        server.quit()
