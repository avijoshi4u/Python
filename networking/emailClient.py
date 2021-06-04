import smtplib
from email.mime.text import MIMEText

body = "This is a test Email. How are you?"

msg = MIMEText(body)
msg['From'] = "sapna333222@gmail.com"
msg['To'] = "sapna333222@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login("sapna333222@gmail.com", "Aarna@172018")
server.send_message(msg)
print("Mail sent")

server.quit()
