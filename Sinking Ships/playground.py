# line = "XX**********************************************************************************************************************************************"
#
# sea_map = [line[i:i + 12] for i in range(0, len(line), 12)]
#
#
# print(sea_map[0][1])
#
#
# sea_map2 = [['*' for _ in range(12)] for _ in range(12)]
#
# print(sea_map2)

#
# ls = [(4,1),(2,1),(3,1),(1,1)]
# ls.sort()
# print(ls)
#
# ls2 = [(1,5), (1,3), (1,2), (1,7)]
# ls2.sort()
# print(ls2)
#
# print()

def avenger_coordinates( hits: list, length: int) -> list:
    already_hit = sorted(hits)
    row, col = already_hit[0]

    if length == 5:
        vertical_offsets = [(0, 0), (-2, -1), (-2, 1)]
        horizontal_offsets = [(0, 0), (1, -2), (-1, -2)]
    elif length == 3:
        vertical_offsets = [(0, 0), (1, -1), (-1, -1)]
        horizontal_offsets = [(0, 0), (2, 1), (-2, 1)]
    else:
        return []

    vertical_coordinates = [(row + v_offset, col + h_offset) for v_offset, h_offset in vertical_offsets]
    horizontal_coordinates = [(row + v_offset, col + h_offset) for v_offset, h_offset in horizontal_offsets]

    return [vertical_coordinates, horizontal_coordinates]

def vertical_avenger_three( hits: list) -> list:
    already_hit = sorted(hits)
    # vztazny bod
    row, col = already_hit[1]
    left = [(row, col - 1), (row, col - 2), (row, col - 3), (row + 1, col - 2), (row - 1, col - 2)]
    right = [(row, col + 1), (row, col + 2), (row, col + 3), (row + 1, col + 2), (row - 1, col + 2)]
    return [left, right]

hits = [(3, 8), (4, 8), (5, 8)]

# For a five in a row avenger ship
# coordinates_five = avenger_coordinates(hits, length=5)

# For a three in a row avenger ship
coordinates_three = avenger_coordinates(hits=hits, length=3)
print(coordinates_three)

cord_3 = vertical_avenger_three(hits=hits)
print(cord_3)

