from ship import Ship


class AvengerShip(Ship):

    def __init__(self, ship_to_destroy):
        super().__init__()
        self.hits = ship_to_destroy.hits
        self.orientation = ship_to_destroy.orientation

    def vertical_avenger_five(self) -> list:
        already_hit = sorted(self.hits)
        row, col = already_hit[0]
        return [(row - 1, col - 1), (row - 1, col + 1), (row - 3, col - 1), (row - 3, col + 1)]

    def horizontal_avenger_five(self) -> list:
        already_hit = sorted(self.hits)
        row, col = already_hit[0]
        return [(row + 1, col - 1), (row + 1, col + 1), (row + 1, col + 3), (row - 1, col + 3)]

    def vertical_avenger_three(self) -> list:
        already_hit = sorted(self.hits)
        row, col = already_hit[1]
        left = [(row, col - 1), (row, col - 2), (row, col - 3), (row + 1, col - 2), (row - 1, col - 2)]
        right = [(row, col + 1), (row, col + 2), (row, col + 3), (row + 1, col + 2), (row - 1, col + 2)]
        return [left, right]

    def horizontal_avenger_three(self) -> list:
        already_hit = sorted(self.hits)
        row, col = already_hit[1]
        upper = [(row + 1, col), (row + 2, col), (row + 3, col), (row + 2, col + 1), (row + 2, col - 1)]
        lower = [(row - 1, col), (row - 2, col), (row - 3, col), (row - 2, col + 1), (row - 2, col - 1)]
        return [upper, lower]

    def get_moves(self) -> list:
        length = len(self.hits)
        if length == 3:
            return [coord for sublist in self.vertical_avenger_three() for coord in sublist] if self.orientation == 'V' else [coord for sublist in self.horizontal_avenger_three() for coord in sublist]
        elif length == 5:
            return [coord for sublist in self.vertical_avenger_five() for coord in sublist] if self.orientation == 'V' else [coord for sublist in self.horizontal_avenger_five() for coord in sublist]

