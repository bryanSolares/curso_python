
class Cliente:
    def __init__(self, codigo, nombre, apellido_paterno, apellido_materno, creditos):
        self.codigo = codigo
        self.nombre: str = nombre
        self.apellido_paterno: str = apellido_paterno
        self.apellido_materno: str = apellido_materno
        self.creditos: int = creditos

    def getCliente(self):
        return tuple([self.codigo, self.nombre, self.apellido_paterno,self.apellido_materno, self.creditos])