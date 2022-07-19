import io
from Frases import Frase

llibre = io.open("document.txt", "r")
linies = llibre.readlines()
llibre.close()

listafinal = []
conjuntofinal = set()
f1 = Frase("")

for frase in linies:
    f1.text = frase
    f1.limpiafrase()
    f1.minuscules()
    listafinal +=  f1.listapalabras()
    conjuntofinal.update(f1.setpalabras())

print(len(listafinal))
print(len(set(listafinal)))
print(listafinal)

# Crear un diccionario vacio

diccionario = {}
for word in conjuntofinal:
    diccionario[word] = listafinal.count(word)

for palabra in diccionario.keys():
    if diccionario[palabra] > 20:
        print(palabra)

print(diccionario)
    
    

