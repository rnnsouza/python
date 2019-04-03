# -*- coding: utf-8 -*-

import smtplib # Usado para enviar o email
from email.mime.multipart import MIMEMultipart # Usado para adiciona vários tipos de conteúdo em um email, textos, anexos...
from email.mime.text import MIMEText # Usado pra por o texto
from email.mime.base import MIMEBase # Usado para por o anexo, qualquer tipo de arquivo
from email import encoders # Usado para encode o anexo de uma forma legível, transforma em base64

fromAddr = "renansouza.puc@gmail.com"
toAddr = "renannunes07@hotmail.com"

msg = MIMEMultipart()

msg["From"] = fromAddr
msg["To"] = toAddr
msg["Subject"] = "Teste de Envio"

body = "Olá! Mensagem de teste de envio!"
msg.attach(MIMEText(body))


filename = "teste.gif"
attachment = open(filename,"rb")

# https://freeformatter.com/mime-types-list.html
# Descobrir o mime type do arquivo que será enviado
"""
SABER QUAL O MIME TYPE DE UM ARQUIVO

import mimetypes
mimetypes.guess_type("teste.gif")[0] # arquivo.extensão
>>> 'teste/gif'
mimetypes.guess_type("teste.gif")[0].split('/')
>>> ["image", "gif"]
"""

mimetype_anexo = mimetypes.guess_type(filename)[0].split('/')
part = MIMEBase(mimetype_anexo[0], mimetype_anexo[1])

part.set_payload((attachment).read()) # set_payload, o que está sendo enviando, no caso um attachment
encoders.encode_base64(part) # deixa de forma legível
part.add_header("Content-Disposition", "attachment; filename = %s" %filename)

# Attach dentro da mensagem do anexo
msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(fromAddr, open("senha.txt").read().strip())
text = msg.as_string()
server.sendmail(fromAddr, toAddr, text)
server.quit()