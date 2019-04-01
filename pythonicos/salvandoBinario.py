# -*- coding: utf-8 -*-

import requests

url = "http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-setup.exe"

r = requests.get(url)
f = open("exit.exe",'ab') # 'ab' -> modo append binário
f.write(r.content)
f.close()