import smtplib
from email.mime.text import MIMEText
from backend.config import settings

def send_email_code(to_email: str, code: str):
    msg = MIMEText(f"Your login code is: {code}")
    msg["Subject"] = "Awesome Cloud 登录验证码"
    msg["From"] = settings.EMAIL_USERNAME
    msg["To"] = to_email

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
    server.sendmail(settings.EMAIL_USERNAME, [to_email], msg.as_string())
    server.quit()
