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

print(diccionario)
