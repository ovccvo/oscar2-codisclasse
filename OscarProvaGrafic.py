from random import randint
from time import sleep
from graficar_1_nomes import grafic

def distancia():
    binari = randint(0,1)
    return binari  #Torna 0 o 1 en funció de que passi una persona o no

llistapersones = []
minuts = 0

while minuts < 2:
    persones=0
    for segons in range(10):
        valors = distancia()        
        persones = persones + valors
        print(persones)
        sleep(1)
    print("persones finals:")
    print(persones)
    llistapersones.append(persones)
    print(llistapersones)
    minuts +=1
grafic(llistapersones)
