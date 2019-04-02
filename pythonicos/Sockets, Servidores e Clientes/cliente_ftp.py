# -*- coding: utf-8 -*-

from ftplib import FTP 

ftp = FTP("pythonicos.com.br")
# user, senha (a senha está dentro de um arquivo texto)
ftp.login("pythonicos", open("senha.txt").read().strip())


### Fazer Download de um Arquivo

# Comando RETR
# nome_arquivo, local_salvar
# Abre um arquivo na minha máquina no modo de escrita binária
ftp.retrbinary("RETR .nome_arquivo",open("arquivo_texto_MaquinaLocal","wb").write)


### Upload de um arquivo

# nome_a_salvar, arquivo_local (o que tenho na máquina)
# Comando STOR 
# builder.txt -> nome que darei ao arquivo que será salvo
# README -> nome do arquivo presente na minha máquina,  que vou fazer upload
ftp.storbinary("STOR builder.txt",open("README.txt","rb"))

###	COMANDOS ### 

'''
FTP("ftp.example.com") - Instância de FTP com o servidor de conexão
login("user","password") - Faz login no servidor instânciado
set_debuglevel(0,1,2) - Altera o nível de debug 
set_pasv(True,False) - Habilita/Desabilita modo passivo
dir() - Lista diretório
rename("original","novo") - Renomeia arquivo
delete("arquivo") - Deleta arquivo
cwd("passwd/") - Altera o diretório
mkd("mundo") - Cria diretório
rmd("mundo") - Exclui diretório
size("arquivo") - Retorna tamanho do arquivo
close() - Fecha conexão

'''