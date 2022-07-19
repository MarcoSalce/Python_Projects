import io

class Frase:
    def __init__(self, text):
        self.text = text
    
    def minuscules(self):
        self.text = self.text.lower()
        
    def limpiafrase(self):
        for letra in self.text:
            if letra not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
               self.text = self.text.replace(letra," ")
           
    def listapalabras(self) :
        return self.text.split()
    
    def setpalabras(self):
        return set(self.listapalabras())
       
    def getfrase(self):         
        self.text = input("")
  
    def __str__(self):
        return f"La cadena es {self.text}"

    
diccionario = {}

l1 = Frase("")
for vocal in 'aeiouàèéíòóúïü':
    diccionario[vocal] = 0

text = io.open('document.txt','r',encoding='utf-8')   #'latin-1' ??????

linies = text.readlines()

for linia in linies:
    l1.text=linia
    l1.minuscules()
    for letra in l1.text:
        if letra in 'aeiouàèéíòóúïü':
            diccionario[letra] += 1

salida = io.open('sortida.txt', 'w') # Esto es para crear el resultado fuera de la consola, y lo exporta a un archivo
salida.write(f"{diccionario}")
salida.close(diccionario)
# Esto ultimo sustituye al print para acelerar el proceso y asi demora menos

# 'r' leer el contenido
# 'w' escribir en un archivo, 'Machaca' lo que habia
# 'a' añade a lo que hubiera con nuevo contenido

#print(diccionario)


