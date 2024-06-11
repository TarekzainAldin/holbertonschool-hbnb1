from models.city import City
from persistence.IPersistenceManager import IPersistenceManager
import uuid
from datetime import datetime

class CityDataManager(IPersistenceManager):
    def __init__(self):
        self.cities = []

    def save(self, city):
        if any(existing_city.name == city.name and existing_city.country_id == city.country_id for existing_city in self.cities):
            raise ValueError("City already exists in this country")
        city.id = str(uuid.uuid4())
        city.created_at = datetime.now()
        city.updated_at = datetime.now()
        self.cities.append(city)
        return city

    def get(self, city_id):
        for city in self.cities:
            if city.id == city_id:
                return city
        return None

    def get_all(self):
        return self.cities

    def update(self, updated_city):
        for idx, city in enumerate(self.cities):
            if city.id == updated_city.id:
                updated_city.updated_at = datetime.now()
                self.cities[idx] = updated_city
                return True
        return False

    def delete(self, city_id):
        for idx, city in enumerate(self.cities):
            if city.id == city_id:
                del self.cities[idx]
                return True
        return False

    def get_cities_by_country(self, country_id):
        return [city for city in self.cities if city.country_id == country_id]
