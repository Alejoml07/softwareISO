from http import client
from pydoc import cli
import random
from curses.ascii import isdigit
from cliente import *
from computador import *

if __name__ == "__main__":
    
    cliente1 = Cliente()
    
    cliente1.idC = random.randint(0, 100)
    n= False
    while n == False:
        nombre = str(input ("Nombre Cliente: "))
        if nombre.isalpha():
            n = True
            cliente1.nombreC = nombre
        if nombre.isalpha() == False:
            n = False
            print("Nombre invalido")
            
            
    t= False
    while t == False:
        telefono = str(input("Telefono cliente: "))
        if telefono.isdigit():
            t = True
            cliente1.telefonoC = telefono
        if telefono.isdigit() == False:
            t = False
            print("Numero invalido")
    
    c = False
    while c == False:
        email = str(input("Email cliente: "))
        if email.endswith(".com") and email.find('@'):
            c = True
            cliente1.emailC = email
        else:
            print('Correo invalido')
            
    
    
    
    while True:
            opt = int (input("""Tipos de servicios ofrecidos
                             1.Dentro de la cuidad 
                             2.Fuera de la cuidad 
                             3.Dentro del establecimieto
                             Tipo de servicio tomado por el cliente  :
                             """))
        
            if opt == 1:
                equipos = int (input("N·mero de equipos que desea alquilar:  "))
                dias = int (input("N·mero de dÝas que desea tomar el alquiler:  "))
                adicionales = int (input("N·mero de dÝas adicionales que toma el alquiler:  "))
                dentro_ciu = Computador(equipos,dias,adicionales)
                
                print (f"Nombre:{cliente1.nombreC}\n"f"Email:{cliente1.emailC}\n"f"Email:{cliente1.idC}\n"f"Telefono: {cliente1.telefonoC}")
                comp = dentro_ciu.alquilarDentroCiudad()
                
                
            elif opt == 2:
                equipos = int (input("N·mero de equipos que desea alquilar:  "))
                dias = int (input("N·mero de dÝas que desea tomar el alquiler:  "))
                adicionales = int(input("N·mero de dÝas adicionales que toma el alquiler:  "))
                fuera_ciu = Computador(equipos,dias,adicionales)
                print (f"Nombre:{cliente1.nombreC}\n","Email:{cliente1.emailC}\n","Email:{cliente1.idC}\n","Telefono: {cliente1.telefonoC}")
                comp = fuera_ciu.alquilarFueraCiudad()
                
                
                
            elif opt == 3:
                equipos = int (input("N·mero de equipos que desea alquilar:  "))
                dias = int (input("N·mero de dÝas que desea tomar el alquiler:  "))
                adicionales = int(input("N·mero de dÝas adicionales que toma el alquiler:  "))
                detro_establecimiento = Computador(equipos,dias,adicionales)
                print (f"Nombre:{cliente1.nombreC}\n","Email:{cliente1.emailC}\n","Email:{cliente1.idC}\n","Telefono: {cliente1.telefonoC}")
                comp = detro_establecimiento.alquilarDentroLocal()

                
            break 

