import unittest
from sea_map import SeaMap  # Import the class you want to test


class TestSeaMap(unittest.TestCase):
    def test_filter_moves_within_grid_and_unknown(self):
        """
        Test the filter_moves method when coordinates are within the grid and unknown.
        """
        sea_map = SeaMap()

        # Mock input coordinates
        coordinates = [(1, 2), (5, 6), (8, 10)]

        # Set grid values to '*'
        sea_map.grid = [['*' for _ in range(12)] for _ in range(12)]

        # Call the method to be tested
        result = sea_map.filter_moves(coordinates)

        # Assertions
        self.assertEqual(result, coordinates, "Filter should not remove any coordinates.")

    def test_filter_moves_outside_grid(self):
        """
        Test the filter_moves method when coordinates are outside the grid.
        """
        sea_map = SeaMap()

        # Mock input coordinates
        coordinates = [(-1, 2), (5, 15), (8, -4)]

        # Set grid values to '*'
        sea_map.grid = [['*' for _ in range(12)] for _ in range(12)]

        # Call the method to be tested
        result = sea_map.filter_moves(coordinates)

        # Assertions
        self.assertEqual(result, [], "Filter should remove coordinates outside the grid.")

    def test_filter_moves_known_positions(self):
        """
        Test the filter_moves method when coordinates are known (not '*').
        """
        sea_map = SeaMap()

        # Mock input coordinates
        coordinates = [(1, 2), (5, 6), (8, 10)]

        # Set grid values to 'X'
        sea_map.grid = [['X' for _ in range(12)] for _ in range(12)]

        # Call the method to be tested
        result = sea_map.filter_moves(coordinates)

        # Assertions
        self.assertEqual(result, [], "Filter should remove known positions.")

    def test_update_map(self):
        """
        Test the update_map method.
        """
        sea_map = SeaMap()

        # Mock input string_map
        string_map = '************............XXXXXXXXXXXX'

        # Call the method to be tested
        sea_map.update_map(string_map)

        # Assertions
        self.assertEqual(sea_map.grid[0][0], '*')
        self.assertEqual(sea_map.grid[0][11], '*')
        self.assertEqual(sea_map.grid[1][0], '.')
        self.assertEqual(sea_map.grid[1][11], '.')
        self.assertEqual(sea_map.grid[2][0], 'X')
        self.assertEqual(sea_map.grid[2][11], 'X')

    def test_get_all_possible_shots(self):
        """
        Test the get_all_possible_shots method.
        """
        sea_map = SeaMap()

        # Set grid values to '*'
        sea_map.grid = [['*' for _ in range(12)] for _ in range(12)]

        # Call the method to be tested
        result = sea_map.get_all_possible_shots()

        # Assertions
        self.assertEqual(len(result), 144, "All positions should be possible shots.")
        self.assertIn((0, 0), result, "(0, 0) should be a possible shot.")
        self.assertIn((11, 11), result, "(11, 11) should be a possible shot.")


# Run the tests
if __name__ == '__main__':
    unittest.main()
