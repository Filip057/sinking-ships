import unittest
from ship import Ship  # Replace 'your_module' with the actual module name


class TestShip(unittest.TestCase):

    def test_get_moves_single_hit(self):
        """
        Test the get_moves method with a single hit.
        """
        # Create a Ship instance
        ship = Ship()

        # Set a single hit
        ship.hits = [(3, 4)]

        # Call the method to be tested
        result = ship.get_moves()

        # Expected result for a single hit
        expected_result = [(4, 4), (2, 4), (3, 5), (3, 3)]

        # Assertions
        self.assertEqual(result, expected_result, "Incorrect moves for a single hit.")

    def test_get_moves_horizontal_pattern(self):
        """
        Test the get_moves method with a horizontal pattern.
        """
        # Create a Ship instance
        ship = Ship()

        # Set hits for a horizontal pattern
        ship.hits = [(3, 4), (3, 5), (3, 6)]

        # Call the method to be tested
        result = ship.get_moves()

        # Expected result for a horizontal pattern
        expected_result = [(3, 3), (3, 7)]

        # Assertions
        self.assertEqual(result, expected_result, "Incorrect moves for a horizontal pattern.")

    def test_get_moves_vertical_pattern(self):
        """
        Test the get_moves method with a vertical pattern.
        """
        # Create a Ship instance
        ship = Ship()

        # Set hits for a vertical pattern
        ship.hits = [(2, 4), (3, 4), (4, 4)]

        # Call the method to be tested
        result = ship.get_moves()

        # Expected result for a vertical pattern
        expected_result = [(1, 4), (5, 4)]

        # Assertions
        self.assertEqual(result, expected_result, "Incorrect moves for a vertical pattern.")

    def test_get_moves_ship_on_edge(self):
        ship = Ship()

        ship.hits = [(3, 0)]

        result = ship.get_moves()

        expected_results = [(2, 0), (4, 0), (3, 1), (3, -1)]

        self.assertCountEqual(result, expected_results, 'Unexpected behaviour')


if __name__ == '__main__':
    unittest.main()
