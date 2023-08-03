class Customer():#definimos clase cliente

    #inicializamos
    def __init__(self, cedula, name=None, whatsapp=None, email=None) -> None:
        self.cedula = cedula
        self.name = name
        self.whatsapp = whatsapp
        self.email = email

    def to_JSON(self):#retornamos un json
        return {
            'cedula': self.cedula,
            'name': self.name,
            'whatsapp': self.whatsapp,
            'email': self.email
        }

"""
este documento selecciona todo los datos y los determina en que posicion y como estara estructurado en base a la tabla de la base
de datos
"""