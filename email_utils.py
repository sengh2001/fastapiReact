import os
from email.message import EmailMessage
from aiosmtplib import send
from dotenv import load_dotenv

load_dotenv()

async def send_contact_email(name: str, email: str, message: str):
    email_msg = EmailMessage()
    email_msg["From"] = os.getenv("EMAIL_USER")
    email_msg["To"] = os.getenv("RECEIVER_EMAIL")
    email_msg["Subject"] = f"New Contact Message from {name}"

    email_msg.set_content(
        f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )

    await send(
        email_msg,
        hostname=os.getenv("EMAIL_HOST"),
        port=int(os.getenv("EMAIL_PORT")),
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASS"),
        start_tls=True,
    )
