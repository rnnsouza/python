# -*- coding: utf-8 -*-

import shutil
import os

print(os.listdir('.'))

### CÓPIA ###

# copiando o arquivo 'Topologias dos Testes' para 'Fotos' que é uma pasta
shutil.copy("Topologias dos Testes.docx",'Fotos')

# movendo o arquivo 'Topologias dos Testes' para 'copia.docx'. copia.docx não existe
# então é criado um novo arquivo chamado copia.docx com o conteúdo passado.
shutil.copy("Topologias dos Testes.docx",'copia.docx')


### MOVENDO ###

# shutil.move(), move ou subscreve o arquivo
# movendo o arquivo 'Topologias dos Testes' para 'Fotos' que é uma pasta
shutil.move("Topologias dos Testes.docx",'Fotos')



### APAGANDO ARQUIVOS E PASTAS (PERMANENTEMENTE) 

# os.unlink(path) - apaga arquivo
# osrmdir(path) - apaga pasta vazia
# shutil.rmtree(path) - apaga pasta seus arquivos e subpastas


# Apagando o arquivo 'arquivoTest.txt'
os.unlink('arquivoTeste.txt')

# Apagando diretório vazio
os.rmdir('pastaTeste')

# Apagando pasta seus arquivos e subpastas
shutil.rmtree('pastaTeste')