import random


class Ship:
    hits = []
    was_hit = False
    destroyed = False
    length = len(hits)
    is_avenger = False
    check_to_do = length == 5
    orientation = None

    possible_moves = []

    def get_moves(self):
        if len(self.hits) == 1:
            row, col = self.hits[0]
            return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        row_diff = self.hits[1][0] - self.hits[0][0]
        col_diff = self.hits[1][1] - self.hits[0][1]

        next_cor = sorted(self.hits)
        if row_diff == 0:
            # horizontal pattern
            self.orientation = 'H'
            return [(next_cor[0][0], next_cor[0][1] - 1), (next_cor[-1][0], next_cor[-1][1] + 1)]
        if col_diff == 0:
            # vertical pattern
            self.orientation = 'V'
            return [(next_cor[0][0] - 1, next_cor[0][1]), (next_cor[-1][0] + 1, next_cor[-1][1])]










