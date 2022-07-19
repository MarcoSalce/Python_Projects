import io

class Frase:
   
    
    def __init__(self, text):
        
        self.text = text
    
    def minuscules(self):
        """ Convierte una frase en minusculas"""
        self.text = self.text.lower()
        
    def limpiafrase(self):
        """ Sustituye los caracteres de la frase que no sean letras o espacios 
        por espacios """
        for letra in self.text:
            if letra not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
               self.text = self.text.replace(letra," ")
           
    def listapalabras(self) :
        """ Convierta la frase en una lista de palabras"""
        return self.text.split()
    
    def setpalabras(self):
        """ Obtiene un set con las palabras distintas"""
        return set(self.listapalabras())
       
    def getfrase(self): 
        """Pregunta que frase quieres convertir en objeto"""    
        self.text = input("")
  
    def __str__(self):
        """ Describe el objeto"""
        return f"La cadena es {self.text}"


llibre = io.open("document.txt","r", encoding = 'utf-8')
linies = llibre.readlines()
llibre.close()

listafinal =[]
conjuntofinal = set()
f1 = Frase("")
for frase in linies:
    f1.text = frase
    f1.limpiafrase()
    f1.minuscules()
    listafinal += f1.listapalabras()
    conjuntofinal.update(f1.setpalabras())

diccionario = {}
salida = io.open("resultat.txt","a")
for word in conjuntofinal:
    diccionario[word] = listafinal.count(word)

for palabra in diccionario.keys():

    if diccionario[palabra] > 50:
        salida.write(palabra +'\n')

print("guarde los resultados en resultat.txt")
salida.close()        
    





