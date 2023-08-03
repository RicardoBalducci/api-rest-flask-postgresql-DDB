#importamos la libreria que nos permite saber datos del dia
import datetime
#clase date formate
class DateFormat():
    @classmethod
    def convert_date(self, date):
        current_datetime = datetime.datetime.now()#creamos una variable que nos guarde, los datos del dia de hoy.
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")#creamos otra variable y mediante el metodo strftime la transformamos a dia-mes-año horas
        return formatted_datetime#por ultimo la retornamos