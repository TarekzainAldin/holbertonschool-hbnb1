from persistence.IPersistenceManager import IPersistenceManager
from models.place import Place

class PlaceDataManager(IPersistenceManager):
    def __init__(self):
        self.places = []

    def validate_place_data(self, data):
        required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(data['latitude'], (float, int)) or not (-90 <= data['latitude'] <= 90):
            raise ValueError("Invalid latitude")
        
        if not isinstance(data['longitude'], (float, int)) or not (-180 <= data['longitude'] <= 180):
            raise ValueError("Invalid longitude")
        
        if not isinstance(data['number_of_rooms'], int) or data['number_of_rooms'] < 0:
            raise ValueError("Invalid number of rooms")
        
        if not isinstance(data['number_of_bathrooms'], int) or data['number_of_bathrooms'] < 0:
            raise ValueError("Invalid number of bathrooms")
        
        if not isinstance(data['price_per_night'], (float, int)) or data['price_per_night'] < 0:
            raise ValueError("Invalid price per night")
        
        if not isinstance(data['max_guests'], int) or data['max_guests'] < 0:
            raise ValueError("Invalid max guests")
        
        # Assuming cities and amenities are pre-loaded
        # Validation for city_id and amenity_ids against pre-loaded data
        pass

    def save(self, place):
        self.validate_place_data(place)
        place_obj = Place(**place)
        place_obj.id = len(self.places) + 1
        self.places.append(place_obj.to_dict())
        return place_obj.to_dict()

    def get(self, place_id):
        for place in self.places:
            if place['id'] == place_id:
                return place
        return None

    def update(self, updated_place):
        self.validate_place_data(updated_place)
        for idx, place in enumerate(self.places):
            if place['id'] == updated_place['id']:
                self.places[idx] = updated_place
                return True
        return False

    def delete(self, place_id):
        for idx, place in enumerate(self.places):
            if place['id'] == place_id:
                del self.places[idx]
                return True
        return False

    def get_all(self):
        return self.places
