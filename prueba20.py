import random
def ordenalista(lista):
    if len(lista)>1:
        medio=len(lista)//2
        izquierda=lista[:medio]
        derecha=lista[medio:]
        print(izquierda,"*"*5,derecha)
        ordenalista(izquierda)
        ordenalista(derecha)
        
    i=0
    j=0
    k=0
    
    
    return print(lista)

longitudlista=int(input("Ingrese la longitud de la lista: "))

lista=[random.randint(0,100) for i in range(longitudlista)]

print(lista)

listaordenada=ordenalista(lista)
