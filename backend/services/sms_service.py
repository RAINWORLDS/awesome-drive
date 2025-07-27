from twilio.rest import Client
from backend.config import settings

def send_sms_code(phone: str, code: str):
    client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)
    message = client.messages.create(
        body=f"Awesome Cloud 登录验证码: {code}",
        from_=settings.TWILIO_PHONE,
        to=phone
    )
    return message.sid
