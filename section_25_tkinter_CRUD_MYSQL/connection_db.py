import mysql.connector
from mysql.connector import Error


class ConnectionDB:
    __HOST = "localhost"
    __USER = "dbeaver"
    __PASSWORD = "dbeaver"
    __DATABASE = "python"
    __PORT = 3306

    def __init__(self):
        pass

    def __init_connection(self):
        try:
            connection = mysql.connector.connect(host=self.__HOST, user=self.__USER, password=self.__PASSWORD,
                                                 database=self.__DATABASE, port=self.__PORT)
            print("Connection Successfully established.")
            return connection
        except Error as err:
            print(f"Error -> {err}")

    def get_all_customers(self):
        try:
            connection = self.__init_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM clientes"
            cursor.execute(query)
            data = cursor.fetchall()

            cursor.close()
            connection.close()
            return data
        except Error as err:
            print(f'Error get all customers -> {err}')

    def get_customer_by_id(self, customer_id):
        try:
            connection = self.__init_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM clientes WHERE codigo = %s"
            cursor.execute(query,[customer_id])
            data = cursor.fetchone()

            cursor.close()
            connection.close()
            return data
        except Error as err:
            print(f'Error get customer -> {err}')

    def insert_customer(self, customer_id, name, last_name_p, last_name_m, credits):
        try:
            connection = self.__init_connection()
            cursor = connection.cursor()
            query = "INSERT INTO clientes (codigo, nombre, apellido_paterno, apellido_materno, creditos) VALUES (%s, %s, %s, %s, %s)"
            data = (customer_id, name, last_name_p, last_name_m, credits)
            cursor.execute(query, data)
            connection.commit()

            cursor.close()
            connection.close()
            print("Customer inserted successfully.")
        except Error as err:
            print(f'Error to insert customer -> {err}')

    def update_customer(self, customer_id, name, last_name_p, last_name_m, credits):
        try:
            connection = self.__init_connection()
            cursor = connection.cursor()
            query = "UPDATE clientes SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, creditos = %s WHERE codigo = %s"
            data = (name, last_name_p, last_name_m, credits, customer_id)
            cursor.execute(query, data)
            connection.commit()

            cursor.close()
            connection.close()
            print("Customer updated successfully.")
        except Error as err:
            print(f'Error to update customer -> {err}')

    def delete_customer(self, customer_id):
        try:
            connection = self.__init_connection()
            cursor = connection.cursor()
            query = "DELETE FROM clientes WHERE codigo = %s"
            cursor.execute(query, [customer_id])
            connection.commit()

            cursor.close()
            connection.close()
            print("Customer deleted successfully.")
        except Error as err:
            print(f'Error to delete customer -> {err}')


