import unittest
from flask import json
from api.amenity_routes import amenity_bp
from persistence.amenity_data_manager  import AmenityDataManager
from api import app

class TestAmenityRoutes(unittest.TestCase):
    def setUp(self):
        app.register_blueprint(amenity_bp)
        self.client = app.test_client()
        self.amenity_manager = AmenityDataManager()

    def test_create_amenity(self):
        data = {'name': 'Pool'}
        response = self.client.post('/amenities', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_amenities(self):
        response = self.client.get('/amenities')
        self.assertEqual(response.status_code, 200)

    def test_get_amenity(self):
        # Add an amenity first
        data = {'name': 'Pool'}
        response = self.client.post('/amenities', json=data)
        self.assertEqual(response.status_code, 201)
        amenity_id = response.json['id']

        # Now fetch the added amenity
        response = self.client.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_amenity(self):
        # Add an amenity first
        data = {'name': 'Pool'}
        response = self.client.post('/amenities', json=data)
        self.assertEqual(response.status_code, 201)
        amenity_id = response.json['id']

        # Update the amenity
        data = {'name': 'Gym'}
        response = self.client.put(f'/amenities/{amenity_id}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_amenity(self):
        # Add an amenity first
        data = {'name': 'Pool'}
        response = self.client.post('/amenities', json=data)
        self.assertEqual(response.status_code, 201)
        amenity_id = response.json['id']

        # Delete the added amenity
        response = self.client.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
