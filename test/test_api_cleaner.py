import unittest
from src.api_cleaner import get_location
from unittest.mock import patch
import requests
class ApiClientTests(unittest.TestCase):
    @patch('src.api_cleaner.requests.get') #se debe colocar el modulo que se esta usando en la funcion
    def test_get_location_returns_expected_data(self,mock_get):
        mock_get.return_value.status_code=200
        mock_get.return_value.json.return_value={
            "countryName": "United States of America",
            "regionName": "California",
            "cityName": "Mountain View"
        }
        result= get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"United States of America")
        self.assertEqual(result.get("region"),"California")
        self.assertEqual(result.get("city"),"Mountain View")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_cleaner.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")


    '''Ejemplo de Deepseek slice effect
    
    mock_get.side_effect = [
    requests.exceptions.Timeout(),
    requests.exceptions.Timeout(),
    unittest.mock.Mock(status_code=200, json=lambda: {"data": "ok"}),]

    # Primera llamada: timeout
    with self.assertRaises(requests.exceptions.Timeout):
        get_location("8.8.8.8")

    # Segunda llamada: timeout
    with self.assertRaises(requests.exceptions.Timeout):
        get_location("8.8.8.8")

    # Tercera llamada: éxito
    result = get_location("8.8.8.8")
    self.assertEqual(result.get("data"), "ok")
    '''
    