# -*- coding: utf-8 -*-
# arquivo que irá fazer todas as chamadas dos outros arquivos

import aleatorio as alt
import media as m

lista = alt.geraListInt(4)
print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("A média da minha lista é: "+str(media))
print("A mediana da minha lista é: "+str(mediana))
print("A moda da minha lista é: "+str(moda))