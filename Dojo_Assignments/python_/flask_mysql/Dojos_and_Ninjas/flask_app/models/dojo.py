from ..config.mysqlconnection import connectToMySQL
from ..models.ninja import Ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query= "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        print("%(id)s")
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls(results[0])
        for row in results: 
            data = {
                "id":row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "age":row['age'],
                "dojos_id":row['dojos_id'],
                "created_at":row['ninjas.created_at'],
                "updated_at":row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(data))

        return dojo