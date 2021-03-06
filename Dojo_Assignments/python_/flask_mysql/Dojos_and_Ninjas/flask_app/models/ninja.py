from ..config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojos_id = data['dojos_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojos_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        ninja_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return ninja_id