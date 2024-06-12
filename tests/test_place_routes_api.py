import unittest
import json
from flask import Flask
from api.place_routes_api import place_bp

class TestPlaceRoutesAPI(unittest.TestCase):
    def setUp(self):
        # Create a Flask app and register the place blueprint
        self.app = Flask(__name__)
        self.app.register_blueprint(place_bp)
        # Create a test client
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_create_place(self):
        # Test creation of a new place
        data = {
            'name': 'Test Place',
            'description': 'A test place',
            'address': '123 Test St',
            'city_id': 1,  # Assuming city_id exists in pre-loaded data
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 1,  # Assuming host_id exists
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenity_ids': [1, 2]  # Assuming amenity_ids exist
        }
        response = self.client.post('/api/v1/places', json=data)
        self.assertEqual(response.status_code, 201, "Failed to create a new place: Unexpected status code")

    def test_get_all_places(self):
        # Test retrieval of all places
        response = self.client.get('/api/v1/places')
        self.assertEqual(response.status_code, 200, "Failed to retrieve all places: Unexpected status code")
        # Check if response is JSON
        self.assertEqual(response.content_type, 'application/json', "Failed to retrieve all places: Response is not JSON")

    def test_get_place(self):
        # Test retrieval of a specific place
        # First, create a test place
        data = {
            'name': 'Test Place',
            'description': 'A test place',
            'address': '123 Test St',
            'city_id': 1,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 1,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenity_ids': [1, 2]
        }
        response = self.client.post('/api/v1/places', json=data)
        self.assertEqual(response.status_code, 201, "Failed to create a new place: Unexpected status code")
        place_id = json.loads(response.data)['id']
        
        # Then, test retrieval of the created place
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200, "Failed to retrieve a specific place: Unexpected status code")

    def test_update_place(self):
        # Test updating a place
        # First, create a test place
        data = {
            'name': 'Test Place',
            'description': 'A test place',
            'address': '123 Test St',
            'city_id': 1,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 1,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenity_ids': [1, 2]
        }
        response = self.client.post('/api/v1/places', json=data)
        self.assertEqual(response.status_code, 201, "Failed to create a new place: Unexpected status code")
        place_id = json.loads(response.data)['id']
        
        # Then, test updating the created place
        updated_data = {
            'id': place_id,
            'name': 'Updated Test Place'
        }
        response = self.client.put(f'/api/v1/places/{place_id}', json=updated_data)
        self.assertEqual(response.status_code, 200, "Failed to update the place: Unexpected status code")

    def test_delete_place(self):
        # Test deletion of a place
        # First, create a test place
        data = {
            'name': 'Test Place',
            'description': 'A test place',
            'address': '123 Test St',
            'city_id': 1,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 1,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenity_ids': [1, 2]
        }
        response = self.client.post('/api/v1/places', json=data)
        self.assertEqual(response.status_code, 201, "Failed to create a new place: Unexpected status code")
        place_id = json.loads(response.data)['id']
        
        # Then, test deletion of the created place
        response = self.client.delete(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 204, "Failed to delete the place: Unexpected status code")

if __name__ == '__main__':
    unittest.main()
