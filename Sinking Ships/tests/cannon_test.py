from cannon import Cannon  # Import the class you want to test

import unittest
from unittest.mock import patch, MagicMock


class TestCannon(unittest.TestCase):
    @patch('requests.get')  # Mock the requests.get function to control its behavior
    def test_fire_at_position(self, mock_requests_get):
        # Set up mock response data
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'grid': '...',
            'cell': 'X',
            'result': True,
            'avengerAvailable': False,
            'mapId': 1,
            'mapCount': 10,
            'moveCount': 5,
            'finished': False
        }

        # Configure the mock to return the mock_response
        mock_requests_get.return_value = mock_response

        # Create an instance of the Cannon class
        cannon = Cannon(headers={}, query_params={}, api_endpoint='example.com')

        # Call the method to be tested
        outcome = cannon.fire_at_position(row=1, col=1)

        # Assertions based on the expected mock response
        self.assertEqual(outcome, 'X')
        self.assertEqual(cannon.grid_info, '...')
        self.assertTrue(cannon.valid_shot)
        self.assertFalse(cannon.avenger_available)
        self.assertEqual(cannon.mapId, 1)
        self.assertEqual(cannon.mapCount, 10)
        self.assertEqual(cannon.moveCount, 5)
        self.assertFalse(cannon.game_finished)

    @patch('requests.get')  # Mock the requests.get function
    def test_get_current_situation(self, mock_requests_get):
        # Set up mock response data
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'grid': '...',
            'cell': '.',
            'result': True,
            'avengerAvailable': True,
            'mapId': 2,
            'mapCount': 10,
            'moveCount': 6,
            'finished': False
        }

        # Configure the mock to return the mock_response
        mock_requests_get.return_value = mock_response

        # Create an instance of the Cannon class
        cannon = Cannon(headers={}, query_params={}, api_endpoint='example.com')

        # Call the method to be tested
        cannon.get_current_situation()

        # Assertions based on the expected mock response
        self.assertEqual(cannon.outcome, '.')
        self.assertEqual(cannon.grid_info, '...')
        self.assertTrue(cannon.valid_shot)
        self.assertTrue(cannon.avenger_available)
        self.assertEqual(cannon.mapId, 2)
        self.assertEqual(cannon.mapCount, 10)
        self.assertEqual(cannon.moveCount, 6)
        self.assertFalse(cannon.game_finished)


# Run the tests
if __name__ == '__main__':
    unittest.main()
