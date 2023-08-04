#llamamos a las librerias y metodos de diferentes archivos
from database.db import get_connection
from .entities.Order import Order


class OrderModel():
    #Método para ver todos los elementos en orden de cedula de las ordenes
    @classmethod
    def get_orders(self):
        try:
            connection = get_connection()#establecemos la conexion
            orders = []

            with connection.cursor() as cursor:
                #SQL para seleccionar todos los elemento de la tabla orders
                cursor.execute("SELECT order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime FROM orders ORDER BY cedula ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    orders.append(order.to_JSON())

            connection.close()
            return orders
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para ver todos los elementos en orden de dia de las ordenes
    @classmethod
    def get_date(self, datetime):
        try:
            connection = get_connection()#establecemos la conexion
            orders = []
            with connection.cursor() as cursor:
                #SQL para seleccionar un solo elemento de la tabla orders
                cursor.execute("SELECT order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime FROM orders WHERE datetime = %s", (datetime,))
                row = cursor.fetchone()
                if row != None:
                    order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    orders.append(order.to_JSON())
            connection.close()
            return orders
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para ver todos los elementos en orden de status de las ordenes
    @classmethod
    def get_status(self, status):
        try:
            connection = get_connection()#establecemos la conexion
            orders = []
            with connection.cursor() as cursor:
                #SQL para seleccionar un solo elemento de la tabla orders
                cursor.execute("SELECT order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime FROM orders WHERE status = %s ", (status,))
                row = cursor.fetchone()
                if row != None:
                    order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    orders.append(order.to_JSON())
            connection.close()
            return orders
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para ver todos los elementos en orden de cedula de las ordenes
    @classmethod
    def get_cedula(self, cedula):
        try:
            connection = get_connection()#establecemos la conexion
            orders = []
            with connection.cursor() as cursor:
                #SQL para seleccionar un solo elemento de la tabla orders
                cursor.execute("SELECT order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime FROM orders WHERE  cedula = %s", (cedula,))
                row = cursor.fetchone()
                if row != None:
                    order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    orders.append(order.to_JSON())
            connection.close()
            return orders
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para buscar una sola orden
    @classmethod
    def get_order(self, order_number):
        try:
            connection = get_connection()#establecemos la conexion

            with connection.cursor() as cursor:
                #SQL para seleccionar un solo elemento de la tabla orders
                cursor.execute("SELECT order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime FROM orders WHERE order_number = %s", (order_number,))
                row = cursor.fetchone()
                order = None
                if row != None:
                    order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    order = order.to_JSON()
            connection.close()
            return order
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra


    #Método para añadir una orden
    @classmethod
    def add_order(self, order):
        try:
            connection = get_connection()#establecemos la conexion

            with connection.cursor() as cursor:
                #SQL para insertar elementos de la tabla orders
                cursor.execute("""INSERT INTO orders (order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (order.order_number, order.quantity, order.payment_method, order.remarks, order.city, order.municipality, order.cedula, order.total, order.payment_screenshot, order.status, order.delivery_amount, order.datetime,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

    #Método para editar status
    @classmethod
    def update_status(self, order, status):
        try:
            connection = get_connection()#establecemos la conexion
            with connection.cursor() as cursor:
                #SQL para cambiar un solo elemento de la tabla orders
                cursor.execute("""UPDATE orders SET status = %s WHERE order_number = %s""", (status, order.order_number))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra


    #Método para añadir imagen
    @classmethod
    def add_img(self, order):
        try:
            connection = get_connection()#establecemos la conexion

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO orders (order_number, quantity, payment_method, remarks, city, municipality, cedula, total, payment_screenshot, status, delivery_amount, datetime)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (order.order_number, order.quantity, order.payment_method, order.remarks, order.city, order.municipality, order.cedula, order.total, order.payment_screenshot, order.status, order.delivery_amount, order.datetime,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()#cerramos la conexión
            return affected_rows
        except Exception as ex:#en caso de error
            raise Exception(ex)#se muestra

"""

"""
