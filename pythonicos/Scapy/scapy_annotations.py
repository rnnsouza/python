# -*- coding: utf-8 -*-

# pip install scapy (primeira opção, ou a opção a baixo)
# wget https://github.com/secdev/scapy/archive/v2.3.2.zip
# 7z x v2.3.2.zip
# cd v2.3.2
# sudo python setup.py install

# Manipulação de pacotes
# Entrar no Prompt e digitar 'scapy'. Todos os comandos abaixo executados no prompt scapy

# Mostra todos os comandos do scapy
lsc()

### ENVIANDO PACOTES

sr() 		# envia pacotes na L3, e fica aguardando respostas
sr1() 		# envia pacotes na L3, finaliza conexão na primeira respsota
srp() 		# envia pacotes na L2, e fica aguardando respostas
srp1()		# envia pacotes na L2, finaliza conexão na priemira resposta
srloop()	# envia e recebe pacotes em loop, L3
srploop() 	# envia e recebe pacotes em loop, L2


# ls(IP)
# Criando pacote ICMP
ping = IP(dst="8.8.8.8")/ICMP()

# Enviando o pacote
sr1(ping)

# Envia o ping direto sem precisar atribuir a uma variavel
sr1(IP(dst="8.8.8.8")/ICMP())
resposta = sr1(IP(dst="8.8.8.8")/ICMP())

resposta.src
resposta.dst

# Representando um ping -t
srloop(IP(dst="8.8.8.8")/ICMP())
# srloop de tamanho 10
srloop(IP(dst="8.8.8.8")/ICMP().count=10)



### SNIFFER

# Forçando a função sniff a pegar 1 pacote
pkt = sniff(count=1)

# vendo tamanho do pacote 
len(pkt)

# vendo a lista completa
pkt.show()

# vendo toda a lista com dados referente ao pacote
pkt[0].show()


# Definir qual interface de rede vou utilizar
# count=0 significa que irá sniffar continuamente
pkt = sniff(count=0,iface='en0') # não necessário passar o iface

# Mostra tudo o que foi trafegado
pkt.summary()

# Recebi o pacote e quero saber se tem algum dado nele
# Podendo verificar se tem alguma informação no pacote capturado
pkt[3].haslayer(Raw)

# Filtro no sniffer, filtrando dados que queremos
# Trazendo todo tráfego TCP na porta 80
pkt = sniff(count=0.filter='tcp and port 80')