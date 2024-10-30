import smtplib

sender = "k@gmail.com"
receiver = "3@gmail.com"
password = ""
subject = "Python email test"
body = "I wrote myself and email from python code"

message = f"""From: Bread Pit {sender}
To: {receiver}
Subject: {subject}\n
{body}"""


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")