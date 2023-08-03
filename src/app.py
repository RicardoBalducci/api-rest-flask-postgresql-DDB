#importamos la librerias de Flask
from flask import Flask
from flask_cors import CORS
#importamos las configuraciones
from config import config
#importamos las rutas
from routes import Customer
from routes import Order

app=Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:9300"}})

#En caso de que la pagina qno exista le mandamos este mensaje de error
def page_not_found(error):
    return "<h1>Pagina no encontrada<h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    #blueprint
    app.register_blueprint(Customer.main,url_prefix='/customers')#redireccion para customers
    app.register_blueprint(Order.main,url_prefix='/orders')#redireccion para orders
    #url_prefix=indicamos cual es la ruta raiz
    #manejador de error
    app.register_error_handler(404,page_not_found)#en caso de error nos lanza el mensaje declarado anteriormente
    app.run()#correr el programa

"""
Estudiantes:
Ricardo Balducci. 28.308.177
Aimel Quijada. C.I.30.729.553
María Marín. C.I.30.414.526
"""
