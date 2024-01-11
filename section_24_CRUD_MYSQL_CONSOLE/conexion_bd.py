import mysql.connector
from mysql.connector import Error
from functions import Cliente

class Connection:
    __config = {
        'host': 'localhost',
        'user': 'dbeaver',
        'password': 'dbeaver',
        'database': 'python',
        'port': 3306
    }

    def __init__(self):
        pass

    def __initConnection(self):
        try:
            connection = mysql.connector.connect(**self.__config)
            print("Conectado correctamente!!!!")
            return connection
        except Error as err:
            print(f"No se pudo establecer conexión a la base de datos: {err}")

    def listData(self):
        rows = []
        try:
            connection = self.__initConnection()
            cursor = connection.cursor()
            query = "SELECT * FROM clientes"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
        except Error as err:
            print("No se pudo obtener información.")
        finally:
            return rows

    def getCustomer(self, id: str):
        try:
            connection = self.__initConnection()
            cursor = connection.cursor()
            query = "SELECT * FROM clientes WHERE codigo = %s"
            params = [id]
            cursor.execute(query, params)
            data = cursor.fetchone()
            cursor.close()
            connection.close()
            return data

        except Error as err:
            print(f"No se pudo obtener información. {err}")

    def insertData(self, cliente: Cliente):
        try:
            connection = self.__initConnection()
            cursor = connection.cursor()
            query = "INSERT INTO clientes values (%s, %s, %s, %s, %s)"
            cursor.execute(query,cliente.getCliente())
            connection.commit()
            print("Registro almacenado correctamente.")
            cursor.close()
            connection.close()
        except Error as err:
            print(f"No se pudo insertar el registro en base de datos. {err}")

    def updateCustomer(self, id: str, cliente: Cliente):
        try:
            connection = self.__initConnection()
            cursor = connection.cursor()
            data = self.getCustomer(id)

            if data is not None:
                query = "UPDATE clientes SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, creditos = %s WHERE codigo = %s"
                cursor.execute(query,
                               [cliente.nombre, cliente.apellido_paterno, cliente.apellido_materno, cliente.creditos,
                                id])
                connection.commit()
                print("Cliente actualizado exitosamente.")
            else:
                print("El cliente deseado no existe en la base de datos.")
            cursor.close()
            connection.close()
        except Error as err:
            print(f"No se pudo actualizar el registro en base de datos. {err}")

    def deleteCustomer(self, id):
        try:
            connection = self.__initConnection()
            cursor = connection.cursor()

            query = "DELETE FROM clientes WHERE codigo = %s"
            cursor.execute(query, [id])
            connection.commit()

            print("Cliente eliminado correctamente")

            cursor.close()
            connection.close()
        except Error as err:
            print(f"No se pudo eliminar el registro en base de datos. {err}")

