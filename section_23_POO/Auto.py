'''
Para definir una clase se utiliza la palabra reservada 'class'
'''

class Auto:
    #Creación de atributos
    marca: str = "Ford"
    modelo: str = "Clasico"
    placa: int = 123456
    color: str = "Negro"

    #Creación de constructores
    # self es una referencia a la propia instancia recien creada que puede contener atributos no necesariamente inicializados al inicio por ejemplo la marca o modelo
    # TODO IMPORTANT: Se debe destacar que __init__ es un método no inicializador y no un constructor, si se desea personalizar la construcción en sí, se debe utilizar __new__
    # TODO: En Python no hay sobrecarga de constructores
    # TODO: La palabra reservada "pass" permite poder continuar con la ejecución de código sin caer en un bloqueo, por ejemplo para el caso del constructor vacío hace que se pueda avanzar sin declarar o escribir algo más de código
    def __init__(self):
        pass

    # TODO: A cada método de clase se deberá pasar por parámetro el valor self
    def operacionSuma(self, numero1, numero2):
        return numero1 + numero2

# Para generar la instancia de una clase no es necesaria la palabra 'new' como puede ser en Java o Javascript
taxi = Auto()
print(taxi.marca, taxi.modelo, taxi.placa, taxi.color)
print(taxi.operacionSuma(10,20))