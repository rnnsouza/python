# -*- coding: utf-8 -*-

import smtplib

# E-mail recipiente
emailFrom = "renansouza.puc@gmail.com"
# E-mail destinatário
emailTo = "renannunes07@hotmail.com"
# Servidor SMTP
smtp = "smtp.gmail.com"

# Inicia instância da função SMTP, onde é especificado o servidor SMTP e a porta
# 587 -> porta em que grande parte dos servidores SMTP trabalham
server = smtplib.SMTP(smtp, 587)
# Defini conexões usando tls
server.starttls()
# Realiza login no servidor de SMTP, passando usuário e senha
server.login(emailFrom, open("senha.txt").read().strip())

# Corpo do e-mail
msg = "My Message"

# Envia e-mail
server.sendmail(emailFrom, emailTo, msg)

# Fecha conexão
server.quit()