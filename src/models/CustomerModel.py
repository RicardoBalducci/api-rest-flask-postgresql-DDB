#llamamos a las librerias y metodos de diferentes archivos
from database.db import get_connection
from .entities.Customer import Customer


class CustomerModel():
    #Método  para ver todos los elementos en orden de cedula de los clientes
    @classmethod
    def get_customers(self):#definicion de Método  listar customers
        try:
            #conexion con la base de datos
            connection = get_connection()
            customers = []#lista donde se almacena

            with connection.cursor() as cursor:#recorrido
                cursor.execute("SELECT cedula, name, whatsapp, email  FROM customer ORDER BY cedula ASC")#declaracion en SQL
                resultset = cursor.fetchall()

                for row in resultset:#recorrido
                    customer = Customer(row[0], row[1], row[2], row[3])#espacios de almacenamiento
                    customers.append(customer.to_JSON())#serializacion en json

            connection.close()#cerramos la conexión
            return customers#retornamos la lista con los elementos
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método  para buscar un solo cliente
    @classmethod
    def get_customer(self, cedula):#pasamos por parametro la cedula
        try:
            connection = get_connection()#establecemos la conexion

            with connection.cursor() as cursor:
                cursor.execute("SELECT cedula, name, whatsapp, email FROM customer WHERE cedula = %s", (cedula,))#seleccionamos todos los elementos que tengan la cedula
                row = cursor.fetchone()

                customer = None
                if row != None:#si la tabla es diferente de null
                    customer = Customer(row[0], row[1], row[2], row[3])#se llenan los espacion
                    customer = customer.to_JSON()#

            connection.close()#cerramos la conexión
            return customer
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para añadir un cliente
    @classmethod
    def add_customer(self, customer):#pasa por parametros una lista con todos los elementos a añadir
        try:
            connection = get_connection()#establecemos la conexion
            with connection.cursor() as cursor:
                #insertamos todos los elementos en la tabla
                cursor.execute("""INSERT INTO customer (cedula, name, whatsapp, email)
                                VALUES (%s, %s, %s, %s)""", (customer.cedula, customer.name, customer.whatsapp, customer.email))
                affected_rows = cursor.rowcount
                connection.commit()
            #cerramos
            connection.close()#cerramos la conexión
            return affected_rows#retornamos
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para editar un cliente
    @classmethod
    def update_customer(self, customer):#pasa por parametros una lista con todos los elementos a añadir
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE customer SET name = %s, whatsapp = %s, email = %s
                                WHERE cedula = %s""", (customer.name, customer.whatsapp, customer.email, customer.cedula))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()#cerramos la conexión
            return affected_rows
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

"""
Este documento se encarga de hacer todo el proceso de recolectar información y realizar las operaciones en SQL
"""