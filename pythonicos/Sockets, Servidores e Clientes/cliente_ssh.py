# -*- coding: utf-8 -*-
# pip install paramiko

import paramiko

ssh = paramiko.SSHClient()
# Sempre irá dar 'Yes' na pergunta de hosts conhecidos
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# password estando em um arquivo de texto
# password = open("pass.txt").read().strip()
ssh.connect(hostname="127.0.0.1",username="usuario",password="senha") 
stdin,stdout,stderr = ssh.exec_command("ls -l")
print(stdout.read()) # .read() para conseguir printar
ssh.close()