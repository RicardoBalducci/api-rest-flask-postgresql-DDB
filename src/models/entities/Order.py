#llamamos al metodo DateFormat de la clase DateFormate
from utils.DateFormate import DateFormat

class Order():#inicializamos

    #inicializamos
    def __init__(self,  order_number, quantity=None, payment_method=None, remarks=None, city=None, municipality=None, cedula=None, total=None, payment_screenshot=None, status=None, delivery_amount=None,  datetime=None) -> None:
        self.order_number = order_number
        self.quantity = quantity
        self.payment_method = payment_method
        self.remarks = remarks
        self.city = city
        self.municipality = municipality
        self.cedula = cedula
        self.total = total
        self.payment_screenshot = payment_screenshot
        self.status = status
        self.delivery_amount =delivery_amount
        self.datetime = datetime

    #funcion json
    def to_JSON(self):
        return {#retornamos
            'order_number': self.order_number,
            'quantity': self.quantity,
            'payment_method': self.payment_method,
            'remarks': self.remarks,
            'city': self.city,
            'municipality': self.municipality,
            'cedula': self.cedula,
            'total': self.total,
            'payment_screenshot': self.payment_screenshot,
            'status': self.status,
            'delivery_amount': self.delivery_amount,
            'datetime': DateFormat.convert_date(self.datetime)
        }

"""
este documento selecciona todo los datos y los determina en que posicion y como estara estructurado en base a la tabla de la base
de datos
"""