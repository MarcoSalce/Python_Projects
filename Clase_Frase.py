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
'''    
f1 = Frase("La.Farola.De.Laredo.La.Farola.De.Laredo!!!!!!")

#f1.getfrase() # te modifico la variable text

#f1.text = " No perdones demasiado,que se acostumbraran a fallarte"

f1.limpiafrase()
f1.minuscules()
original = f1.listapalabras()
palabrasdistintas =f1.setpalabras()

print(original)
print(palabras distintas)

f2 = Frase("Beneficios infinitos con recursos limitados...no capitalismo!!!")

#f1.getfrase() # te modifico la variable text

#f1.text = " No perdones demasiado,que se acostumbraran a fallarte"

f2.limpiafrase()
f2.minuscules()
original = f2.listapalabras()
palabrasdistintas =f2.setpalabras()    
print(original)
print(palabras distintas)
'''