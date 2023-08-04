#Nos permiten manejar las rutas 
from flask import Blueprint, jsonify, request, render_template
import base64
import os
#utils
from utils.DateFormate import DateFormat
from utils.order_number import OrderNumber
#creamos un plano para manejar las rutas
from flask import Blueprint, jsonify
# Entities
from models.entities.Order import Order
# Models
from models.OrderModel import OrderModel

main = Blueprint('pedido_blueprint',__name__)

#Ruta para ver todos los elementos
@main.route('/')#
def get_orders():#llamamos a todos los elementos
    try:#manejo de excepcion
        datetime = request.args.get('date')#buscamos como argumento el dato date
        status = request.args.get('status')#buscamos como argumento el dato status
        cedula = request.args.get('cedula')#buscamos como argumento el dato cedula
        if datetime:
            orders = OrderModel.get_date(datetime)
            if orders != None:#si order es diferente de None
                return jsonify(orders)#retorna un json de order
            else:
                return jsonify({'message':'ocurrio un error'}), 404#si no muestra un error
        if status:
            orders = OrderModel.get_status(status)
            if orders != None:#si order es diferente de None
                return jsonify(orders)#retorna un json de order
            else:
                return jsonify({'message':'ocurrio un error'}), 404#si no muestra un error
        if cedula:
            orders = OrderModel.get_cedula(cedula)#llamamos a la funcion ger_orders de OrderModel y la guardamos en orders
            if orders != None:#si order es diferente de None
                return jsonify(orders)#retorna un json de order
            else:
                return jsonify({'message':'ocurrio un error'}), 404#si no muestra un error
        orders = OrderModel.get_orders()#llamamos a la funcion ger_orders de OrderModel y la guardamos en orders
        return jsonify(orders)#Aqui se retorna en json y se muestra
    except Exception as ex:#en caso de error
        return jsonify({'message': str(ex)}), 500#muestra mensaje de error

#Buscar un orden en particular
@main.route('/<order_number>')
def get_order(order_number):#llamamos a un  elemento
    try:#manejo de excepcion
        order = OrderModel.get_order(order_number)#llamamos a la funcion get_order de OrderModel y la guardamos en order
        if order != None:#si order es diferente de None
            return jsonify(order)#retorna un json de order
        else:
            return jsonify({'message':'ocurrio un error'}), 404#si no muestra un error
    except Exception as ex:#en caso de error
        return jsonify({'message': str(ex)}), 500#muestra mensaje de error
        
#Ingresar Orden
@main.route('/', methods=['POST'])
def add_order():#añadimos una orden
    try:
        order_number = str(OrderNumber.Generate())#llamamos a la funcion OrderNumber.Generate para que genere un numero aleatorio
        quantity = request.json['quantity']
        payment_method = request.json['payment_method']
        remarks = request.json['remarks']
        city = request.json['city']
        municipality = request.json['municipality']
        cedula = request.json['cedula']
        total = '$12.00'
        payment_screenshot = None
        status = 'pending'
        delivery_amount = '$2.00'
        datetime = DateFormat.convert_date('%Y-%m-%d %H:%M:%S')#llamamos a la funcion convert_date para que llene por defecto el dia
        #ingresamos todos los datos
        order = Order(order_number, quantity, payment_method, remarks, city ,municipality, cedula, total,payment_screenshot, status, delivery_amount , datetime)
        affected_rows = OrderModel.add_order(order)
        if affected_rows == 1:
            return get_order(order_number)
        else:
            return jsonify({'message': "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500#listo

#Editar status de la orden
@main.route('/<order_number>/status', methods=['PATCH'])
def update_status(order_number):
    try:
        status = request.json['status']
        order = Order(order_number, status)
        affected_rows = OrderModel.update_status(order, status)
        if affected_rows == 1:
            return get_order(order_number)
        else:
            return jsonify({'message': "error al modificar"}), 404#en caso de error mostramos
    except Exception as ex:#en caso de error mostramos
        return jsonify({'message': str(ex)}), 500#en caso de error mostramos
        
#imagen
@main.route('/<order_number>/payment-screenshot', methods=['POST'])
def add_img(order_number):
    try:
        return jsonify({'message':'pass'})
    except Exception as ex:#en caso de error mostramos
        return jsonify({'message': str(ex)}), 500#en caso de error mostramos
