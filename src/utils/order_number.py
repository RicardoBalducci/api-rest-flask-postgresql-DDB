#Importamos libreria random
import random

#Creamos una clase llamada orden numero
class OrderNumber():
    @classmethod#METODO DE LA CLASE
    def Generate(self):#creamos un metodo que genere numeros
        return random.randint(1000, 9999)#retornando, generamos que cada vez que se llame esta funcion, retornara un numero entre el rango (1000,9999)
