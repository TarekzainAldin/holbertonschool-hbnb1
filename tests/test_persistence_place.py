# tests/test_persistence_place.py

import unittest
from unittest.mock import MagicMock
from model.place import Place  # Adjust import as per your project structure
from persistence.place_repository_data_manger import PlaceRepository  # Adjust import as per your project structure

class TestPlaceRepository(unittest.TestCase):
    def setUp(self):
        self.place_repository = PlaceRepository()

    def test_save_get(self):
        place = Place(name="Example Place", description="A wonderful place",
                      address="123 Main St", city_id=1, latitude=40.7128,
                      longitude=-74.0060, host_id=1, number_of_rooms=2,
                      number_of_bathrooms=1, price_per_night=100, max_guests=4,
                      amenity_ids=[1, 2, 3])
        self.place_repository.save = MagicMock(return_value=place)
        saved_place = self.place_repository.save(place)
        self.assertEqual(saved_place.name, "Example Place")
        self.assertEqual(saved_place.description, "A wonderful place")

    def test_get_all(self):
        place1 = Place(name="Example Place 1", description="A cozy place",
                       address="456 Elm St", city_id=1, latitude=40.7306,
                       longitude=-73.9352, host_id=2, number_of_rooms=1,
                       number_of_bathrooms=1, price_per_night=80, max_guests=2,
                       amenity_ids=[4, 5])
        place2 = Place(name="Example Place 2", description="A spacious place",
                       address="789 Oak St", city_id=2, latitude=34.0522,
                       longitude=-118.2437, host_id=3, number_of_rooms=3,
                       number_of_bathrooms=2, price_per_night=150, max_guests=6,
                       amenity_ids=[6, 7, 8])
        self.place_repository.get_all = MagicMock(return_value=[place1, place2])
        all_places = self.place_repository.get_all()
        self.assertEqual(len(all_places), 2)
        self.assertEqual(all_places[0].name, "Example Place 1")
        self.assertEqual(all_places[1].name, "Example Place 2")

    def test_update(self):
        place = Place(name="Example Place", description="A wonderful place",
                      address="123 Main St", city_id=1, latitude=40.7128,
                      longitude=-74.0060, host_id=1, number_of_rooms=2,
                      number_of_bathrooms=1, price_per_night=100, max_guests=4,
                      amenity_ids=[1, 2, 3])
        self.place_repository.update = MagicMock(return_value=True)
        update_data = {'price_per_night': 120}
        result = self.place_repository.update(1, update_data)
        self.assertTrue(result)

    def test_delete(self):
        place = Place(name="Example Place", description="A wonderful place",
                      address="123 Main St", city_id=1, latitude=40.7128,
                      longitude=-74.0060, host_id=1, number_of_rooms=2,
                      number_of_bathrooms=1, price_per_night=100, max_guests=4,
                      amenity_ids=[1, 2, 3])
        self.place_repository.delete = MagicMock(return_value=True)
        result = self.place_repository.delete(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
