#llamando bibliotecas
import psycopg2
from psycopg2 import DatabaseError
from decouple import config#permitira

def get_connection():
    try:#usando exception
        return psycopg2.connect(#retornamos la conexion
            host=config('PGSQL_HOST'),#host
            user=config('PGSQL_USER'),#nombre de usuario
            password=config('PGSQL_PASSWORD'),#contraseña
            database=config('PGSQL_DATABASE'),#nombre de la base de datos
        )
    except DatabaseError as ex:# en caso de error
        raise ex#nos lo muestra