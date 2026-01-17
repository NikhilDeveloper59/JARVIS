import smtplib
from email.message import EmailMessage

def send_email(recever,subject,body):
    sender_email = "nraaz590@gmail.com"
    app_password = "jckjcdcmu99oijo"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recever
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:  # 465 (SSL) or 587 (TLS)
            smtp.login(sender_email,app_password)
            smtp.send_message(msg)
            return True
    except Exception as e:
        print(f"Email Error:{e}")
        return False
