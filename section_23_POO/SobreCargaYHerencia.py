
class Persona:
    def __init__(self, nombre = "", apellido = "", edad = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es: {self.nombre} {self.apellido} y tengo {self.edad} años de edad")

    def aumentarEdad(self):
        print(f"Mi edad actual es {self.edad}")
        self.edad += 1
        print(f"Mi nueva edad es de {self.edad}")

    def __str__(self):
        return f"ESTA ES UNA INSTANCIA DE LA CLASE {self.__class__}"

class Bryan(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)

    def aumentarEdad(self):
        print(f"Mi edad actual es {self.edad}")
        self.edad += 2
        print(f"Mi nueva edad es de {self.edad}")

persona1 = Persona()
persona1.saludar()
persona1.aumentarEdad()
print(persona1)

bryan = Bryan("Bryan", "Solares", 28)
bryan.saludar()
bryan.aumentarEdad()
print(bryan)
print("\n************************************")
class Video:
 def __init__(self):
    pass
 def play(self):
     print("Play Video")

class Photo:
    def __init__(self):
        pass
    def takePhoto(self):
        print("Taking photo")


class Smarthphone(Video, Photo):
    def __init__(self, tag):
        self.name = "Smarthphone"
        self.tag = tag

    def showName(self):
        print(self.name)


samsung = Smarthphone("Samsung")
samsung.showName()
samsung.takePhoto()
samsung.play()

# TODO: Cuando se hace herencia, posterior a nombrar la clase, dentro de parentesís se coloca la o las clases de donde se heredará
# TODO: Cuando se utiliza el método super ya no es necesario pasar el parámetro self
# TODO: Los métodos mágicos (__init__, __str__, __repr__) son métodos que modifican comportamientos de la clase por defecto (similiar al toString de Java)