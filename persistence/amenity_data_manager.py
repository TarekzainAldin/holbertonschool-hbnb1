class AmenityDataManager:
    def __init__(self):
        self.amenities = []

    def save(self, amenity):
        amenity['id'] = str(len(self.amenities) + 1)
        self.amenities.append(amenity)
        return amenity

    def get(self, amenity_id):
        for amenity in self.amenities:
            if amenity['id'] == amenity_id:
                return amenity
        return None

    def get_all(self):
        return self.amenities

    def get_by_name(self, name):
        for amenity in self.amenities:
            if amenity['name'] == name:
                return amenity
        return None

    def update(self, updated_amenity):
        for idx, amenity in enumerate(self.amenities):
            if amenity['id'] == updated_amenity['id']:
                self.amenities[idx] = updated_amenity
                return True
        return False

    def delete(self, amenity_id):
        for idx, amenity in enumerate(self.amenities):
            if amenity['id'] == amenity_id:
                del self.amenities[idx]
                return True
        return False
