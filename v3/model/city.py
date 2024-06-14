import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class City:
    def __init__(self, name, country):
        self.city_id = uuid.uuid4().hex
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.country = country

    def save(self):
        city_data = {
            'city_id': self.city_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'country': self.country
        }
        data_manager.create_entity('City', city_data)

    @staticmethod
    def get_by_id(city_id):
        city_data = data_manager.get_entity_by_id('City', city_id)
        if city_data:
            return City(city_data['name'], city_data['country'])
        return None

    @staticmethod
    def update(city_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('City', city_id, updated_data)

    @staticmethod
    def delete(city_id):
        data_manager.delete_entity('City', city_id)

    @staticmethod
    def get_all():
        return data_manager.get_entities('City')

