# 1. row
# 2. column
class SeaMap:
    def __init__(self):
        self.grid = [['*' for _ in range(12)] for _ in range(12)]


        self.signs = {
            '*': 'unknown',
            '.': 'water',
            'X': 'hit'
        }

    # works like a filter, receives list of tuples - coordinates, and checks if
    def filter_moves(self, coordinates: list) -> list:
        filtered_coordinates = []

        for coord in coordinates:
            row, column = coord

            is_within_grid = 0 <= row < 12 and 0 <= column < 12
            try:
                is_unknown = self.grid[row][column] == '*'
            except IndexError:
                is_unknown = False

            if is_within_grid and is_unknown:
                filtered_coordinates.append(coord)

        return sorted(filtered_coordinates)

    def update_map(self, string_map):
        self.grid = [string_map[i:i + 12] for i in range(0, len(string_map), 12)]

    def get_all_possible_shots(self) -> list:
        unknown_positions = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "*":
                    unknown_positions.append((row, col))
        return unknown_positions
