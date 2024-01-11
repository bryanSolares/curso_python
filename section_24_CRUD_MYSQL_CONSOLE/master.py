from conexion_bd import Connection
from functions import Cliente
from datetime import datetime
import random

def menuPrincipal():

    continuar = True
    opcion = 0
    while continuar:
        print("\n**** Bienvenido ****\n")
        print("**** MENU PRINCIPAL ****")
        print("--- CLIENTES ---")
        print("1) Listar")
        print("2) Registrar")
        print("3) Actualizar")
        print("4) Borrar")
        print("5) Salir")
        opcion = int(input("Ingrese la opción que desea:"))
        if opcion > 0 and opcion < 6:
            if opcion == 1: # Listar clientes
                data = Connection().listData()
                if len(data) > 0:
                    print(data)
                else:
                    print("No existe clientes.")
            elif opcion == 2: # Agregar cliente
                cliente = Cliente(datetime.now().timestamp(), "Yojana", "Vicente", "Gomez", random.randint(1,1000))
                Connection().insertData(cliente)

            elif opcion == 3: # Actualizar cliente
                cliente = Cliente(datetime.now().timestamp(),"Yojana--", "Vicente--", "Gomez--", random.randint(1, 1000))
                Connection().updateCustomer(2000, cliente)

            elif opcion == 4: # Borrar cliente
                Connection().deleteCustomer(1)

            elif opcion == 5: # Salir
                continuar = False
        else:
            print("Opcion incorrecta por favor introducir un valor correcto.")


menuPrincipal()