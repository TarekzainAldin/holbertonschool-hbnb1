import unittest
from unittest.mock import patch, MagicMock
from api.app import app
from models.country import Country

class TestCountryCityAPI(unittest.TestCase):

    @patch('api.country_city_routes.country_manager', spec=MagicMock)
    def test_get_countries(self, mock_country_manager):
        mock_countries = [Country(name="Country1", code="C1"), Country(name="Country2", code="C2")]
        mock_country_manager.get_all.return_value = mock_countries

        with app.test_client() as client:
            response = client.get('/api/countries')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [country.to_dict() for country in mock_countries])

    @patch('api.country_city_routes.country_manager', spec=MagicMock)
    def test_get_country(self, mock_country_manager):
        mock_country = Country(name="Country1", code="C1")
        mock_country_manager.get.return_value = mock_country

        with app.test_client() as client:
            response = client.get('/api/countries/C1')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, mock_country.to_dict())

    @patch('api.country_city_routes.country_manager', spec=MagicMock)
    def test_create_country(self, mock_country_manager):
        mock_saved_country = Country(name="New Country", code="NC")
        mock_country_manager.save.return_value = mock_saved_country

        with app.test_client() as client:
            response = client.post('/api/countries', json={"name": "New Country", "code": "NC"})

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, mock_saved_country.to_dict())

    @patch('api.country_city_routes.country_manager', spec=MagicMock)
    def test_update_country(self, mock_country_manager):
        mock_updated_country = Country(name="Updated Country", code="C1")
        mock_country_manager.update.return_value = mock_updated_country

        with app.test_client() as client:
            response = client.put('/api/countries/C1', json={"name": "Updated Country"})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, mock_updated_country.to_dict())

    @patch('api.country_city_routes.country_manager', spec=MagicMock)
    def test_delete_country(self, mock_country_manager):
        mock_country_manager.delete.return_value = True

        with app.test_client() as client:
            response = client.delete('/api/countries/C1')

            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
