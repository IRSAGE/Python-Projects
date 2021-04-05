from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "forjusttestingonly@gmail.com"
message["to"] = "sibo.egide98@gmail.com"
message["subject"] = "This Is A Message From Python"
message.attach(MIMEText("Cool This Actural Working"))

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("forjusttestingonly@gmail.com", "forjusttestingonly98")
    smtp.send_message(message)
    print("sent...")
  
