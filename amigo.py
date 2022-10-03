# importar la función que devolverá una instancia de una conexión
from unittest import result
from amigos_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos


class Amigos:
    db_name="amigos_db"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ocupacion = data['ocupacion']
        self.creador_en = data['creador_en']
        self.actualizado_en = data['actualizado_en']
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(cls.db_name).query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append(cls(friend))
        #retornamos una lista de objetos
        return friends
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO amigos ( nombre, apellido , ocupacion , creador_en, actualizado_en ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        #*!data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_un_amigo(cls, data):
        query = "SELECT * FROM amigos WHERE id=%(identificador)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data )
        return result
