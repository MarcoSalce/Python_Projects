import io

poblacions = io.open("Poblacio_Municipis_2021.csv",'r',encoding = 'utf-8')

llista_registres =  poblacions.readlines()

poblacions.close()
for pos in range(len(llista_registres)):
    llista_registres[pos] = llista_registres[pos].split(';')

salida = io.open('salida.txt','w',encoding = 'utf-8')

for registre in llista_registres:
    salida.write(f"{registre}\n")
salida.close()



    

