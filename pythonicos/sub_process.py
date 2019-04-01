# -*- coding: utf-8 -*-

import subprocess

# Retorna 0 se Sucesso e 1 se Falha. Cada comando entra como se fosse uma lista
process = subprocess.run(['python','--version']) 

# Irá executar o comando dir no windows
a = subprocess.run('dir',shell=True)



# Popen()
# Redireciona os valores de saída para uma variável

process = subprocess.Popen('python --version',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
result =process.communicate()
print(result)