# -*- coding: utf-8 -*-
# pip install paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/.../id_rsa") # caminho até a chave
ssh.connect(hostname="127.0.0.1", username="user", pkey=key)
stdin,stdout,stderr = ssh.exec_command("whoami")
print(stdout.read())
ssh.close()