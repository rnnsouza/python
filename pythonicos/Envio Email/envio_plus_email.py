# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

fromAddr = "renansouza.puc@gmail.com"
toAddr = ["renannunes07@hotmail.com", "outro_email@...."] # uma lista contendo vários e-mails

# msg = MIMEText(open("email.txt","rb").read()) 
msg = MIMEText(open("email.txt").read().strip()) 
msg["From"] = "Renan "
msg["To"] = "Renan Souza"
msg["Subject"] = "Envio Teste"

# Transformando tudo em uma string
msg = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(fromAddr, open("senha.txt").read().strip())
server.sendmail(fromAddr, toAddr, msg)
server.quit()