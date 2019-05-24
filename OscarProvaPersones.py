from random import randint
from time import sleep
import cayenne.client

def cayene(valors):
    persones = valors
    client.virtualWrite(1, persones, "Comptador", "Persones")

def distancia():
    binari = randint(0,1)
    return binari  #Torna 0 o 1 en funció de que passi una persona o no



MQTT_USERNAME = "369ba300-7c78-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "0c7dd6201ff5e6e6044f2f1feace7791ed876715"
MQTT_CLIENT_ID = "3e978d30-7c78-11e9-9636-f9904f7b864b"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

while True:
    client.loop()
    persones=0
    for segons in range(60):
        valors = distancia()        
        persones = persones + valors
        print(persones)
        sleep(1)
    cayene(persones)
    print("persones finals:")
    print(persones)
        
    
