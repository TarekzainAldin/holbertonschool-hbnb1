import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class Country:
    def __init__(self, name):
        self.country_id = uuid.uuid4().hex
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.cities = []  # List to store city objects

    def save(self):
        city_ids = [city.city_id for city in self.cities]
        country_data = {
            'country_id': self.country_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'cities': city_ids
        }
        data_manager.create_entity('Country', country_data)

    @staticmethod
    def get_by_id(country_id):
        country_data = data_manager.get_entity_by_id('Country', country_id)
        if country_data:
            country = Country(country_data['name'])
            country.country_id = country_data['country_id']
            country.created_at = country_data['created_at']
            country.updated_at = country_data['updated_at']
            country.cities = [City.get_by_id(city_id) for city_id in country_data['cities']]
            return country
        return None

    @staticmethod
    def update(country_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('Country', country_id, updated_data)

    @staticmethod
    def delete(country_id):
        data_manager.delete_entity('Country', country_id)

    @staticmethod
    def get_all():
        countries_data = data_manager.get_entities('Country')
        countries = []
        for country_data in countries_data:
            country = Country(country_data['name'])
            country.country_id = country_data['country_id']
            country.created_at = country_data['created_at']
            country.updated_at = country_data['updated_at']
            country.cities = [City.get_by_id(city_id) for city_id in country_data['cities']]
            countries.append(country)
        return countries

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            self.updated_at = datetime.now(timezone.utc).isoformat()
            self.save()

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            self.updated_at = datetime.now(timezone.utc).isoformat()
            self.save()
