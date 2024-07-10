import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "u2203052@rajagiri.edu.in"
receiver_email = "arunvijo2004@gmail.com"
password = "wlvp jkjo kani acts"

message = MIMEMultipart("alternative")
message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email


html = """\
<html>
  <body>
    <p>Hi,<br>
       This is a <b>test email</b>
    </p>
  </body>
</html>
"""


part1 = MIMEText(html, "html")

message.attach(part1)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")