import json 
from .base_model import BaseModel
import uuid
from datetime import datetime

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.id = str(uuid.uuid4())  # Convert uuid to string
        self.name = name
        self.country_id = country.id
        self.country = country
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            self.updated_at = datetime.now()

    def get_place(self):
        return self.places

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "places": self.places
        }

    @classmethod
    def from_json(cls, json_data):
        city_data = json.loads(json_data)
        city = cls(city_data["name"], city_data["country_id"])
        city.id = city_data["id"]
        city.created_at = datetime.fromisoformat(city_data["created_at"])
        city.updated_at = datetime.fromisoformat(city_data["updated_at"])
        city.places = city_data["places"]
        return city

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)
