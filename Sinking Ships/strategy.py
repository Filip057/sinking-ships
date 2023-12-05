# strategy for each map
class Strategy:

    def __init__(self):
        # this dictionary keeps how many ships letf to destroy
        self.ships_left = [2, 3, 3, 4, 5]

    # this method checks if given type of ship is destroyed
    def is_this_ship_destroyed(self, type_of_ship):
        return type_of_ship not in self.ships_left

    # removing destroyed ship
    def remove_destroyed_ship(self, type_of_ship):
        if type_of_ship in self.ships_left:
            self.ships_left.remove(type_of_ship)

    def vertical_avenger_five(self, hits: list) -> list:
        already_hit = sorted(hits)
        # vztazny bod
        row, col = already_hit[0]
        return [(row - 1, col - 1), (row - 1, col + 1), (row - 3, col - 1), (row - 3, col + 1)]

    def horizontal_avenger_five(self, hits: list) -> list:
        already_hit = sorted(hits)
        # vztazny bod
        row, col = already_hit[0]
        return [(row + 1, col - 1), (row + 1, col + 1), (row + 1, col + 3), (row - 1, col + 3)]

    def vertical_avenger_three(self, hits: list) -> list:
        already_hit = sorted(hits)
        # vztazny bod
        row, col = already_hit[1]
        left = [(row, col - 1), (row, col - 2), (row, col - 3), (row + 1, col - 2), (row - 1, col - 2)]
        right = [(row, col + 1), (row, col + 2), (row, col + 3), (row + 1, col + 2), (row - 1, col + 2)]
        return [left, right]

    def horizontal_avenger_three(self, hits: list) -> list:
        already_hit = sorted(hits)
        # vztazny bod
        row, col = already_hit[1]
        upper = [(row + 1, col), (row + 2, col), (row + 3, col), (row + 2, col + 1), (row + 2, col - 1)]
        lower = [(row - 1, col), (row - 2, col), (row - 3, col), (row - 2, col + 1), (row - 2, col - 1)]
        return [upper, lower]

    def avenger_rest_coordinates(self, hits: list, orientation: str) -> list:
        length = len(hits)
        fnc_three = {
            'H': self.horizontal_avenger_three(hits=hits),
            'V': self.vertical_avenger_three(hits=hits)
        }
        fnc_five = {
            "H": self.horizontal_avenger_five(hits=hits),
            "V": self.vertical_avenger_five(hits=hits)
        }
        if length == 3:
            return fnc_three[orientation]
        elif length == 5:
            return fnc_five[orientation]

