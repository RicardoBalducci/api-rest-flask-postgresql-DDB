from flask import Blueprint, jsonify, request
# Entities
from models.entities.Customer import Customer
# Models
from models.CustomerModel import CustomerModel

main = Blueprint('cliente_blueprint',__name__)
#Listar clientes
@main.route('/')
def get_customers():
    try:
        customers = CustomerModel.get_customers()
        return jsonify(customers)#Aqui ya muestra lo que se supone que son
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500#LISTO

#Buscar un cliente en particular
@main.route('/<cedula>')
def get_customer(cedula):
    try:
        customer = CustomerModel.get_customer(cedula)
        if customer != None:
            return jsonify(customer)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500#LISTO


        
#Ingresar CLientes
@main.route('/', methods=['POST'])
def add_customer():
    try:#manejo de excepcion
        #ingresamos los datos
        name = request.json['name']
        whatsapp = int(request.json['whatsapp'])
        email = request.json['email']
        cedula = request.json['cedula']
        customer = Customer(cedula, name, whatsapp, email)

        affected_rows = CustomerModel.add_customer(customer)#llamamos a la funcion add_customer de CustomerModel, para que se incluyan

        if affected_rows == 1:
            return get_customer(cedula)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500#listo

#Editar información de la persona por el metodo PUT
@main.route('/<cedula>', methods=['PUT'])
def update_customer(cedula):
    try:
        name = request.json['name']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        customer = Customer(cedula, name, whatsapp, email)

        affected_rows = CustomerModel.update_customer(customer)

        if affected_rows == 1:
            return get_customer(cedula)
        else:
            return jsonify({'message': "No customer updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



"""
    """