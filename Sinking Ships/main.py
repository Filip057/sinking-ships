
import random

from ship import Ship
from sea_map import SeaMap
from cannon import Cannon
from strategy import Strategy
from avenger_ship import AvengerShip

API_FIRE = 'https://europe-west1-ca-2023-dev.cloudfunctions.net/battleshipsApi/fire/'

API_KEY = 'YtSH2VsDBeb5UDuh51GSiMRxDXA3.w0GXefUWaXekJslEyfXdqmzVlIHOEBMPXcD0mLnkbQUGjOnhFiO2jpxICv0RWKB24WVxXTw0VYRUGLo3wPu0LyUb6pE1zU6krUIQX4Ea2s8pBN1qGFfGKQ38tctXrbwzOhznRTAaPjadoIoF6XOrlemXbjxpUJ8KkGXu0mRZfVeBhRM19Jm1RTkrYFuLRYg64EbI8tWb9mlLvF3Cqf1OtiWuDVEQrJdC3GcPsyFT4vfJKtBdETkuqanZ0IC9V8NO'

HEADERS = {'Authorization': f'Bearer {API_KEY}'}

QUERY_PARAMS = {
    "test": 'yes'
}
API_RESET = "https://europe-west1-ca-2023-dev.cloudfunctions.net/battleshipsApi/reset/"


# tadz prvni inicializace, nacteni mapy, ID mapy
# response = requests.get(url=API_FIRE, params=QUERY_PARAMS, headers=HEADERS)
#
# data = response.json()
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Error: {response.status_code}")
# map in matrix


# def reset_game():
#     import requests 
#     response = requests.get(url=API_RESET, params=QUERY_PARAMS, headers=HEADERS)
#     return response.json()
#
#
# reset = reset_game()
# print(reset)


sea_map = SeaMap()
strategy = Strategy()

num_of_tries = 0
# num_of_maps = 0

# this cycle is for one game
# that means 200 maps
while num_of_tries < 50:
# while mapcount < 200

    # creating objects
    ship_to_destroy = Ship()
    cannon = Cannon(headers=HEADERS, query_params=QUERY_PARAMS, api_endpoint=API_FIRE)

    # updating current map
    cannon.get_current_situation()
    sea_map.update_map(cannon.grid_info)
    print("---------------------------------------\n")
    print("////////SEARCH_FOR_SHIP/////////////////////////\n")
    print("---------------------------------------\n")
    print("/////////STATUS//////////////////////////\n")
    print(f"number of tries:{num_of_tries}")
    print(f" CURRENT MAP: {cannon.mapId}")
    # check if we have found ship, if not fire random shot
    print(f"Before firing: Ship hits: {ship_to_destroy.hits}, Cannon grid info: {cannon.grid_info}")
    print("Fire at random place")
    if not ship_to_destroy.was_hit:
        print(f"REMAINING_SHIP: {strategy.ships_left}")
        # choice from random possible coordinates
        row, column = random.choice(sea_map.get_all_possible_shots())
        print(f"chosen coordinates {(row, column)}")
        # fire at random positions
        cannon.fire_at_position(row=row, col=column)
        # update sea map after shot
        sea_map.update_map(cannon.grid_info)
        print(f"AFTER firing: Ship hits: {ship_to_destroy.hits}, Cannon grid info: {cannon.grid_info}")
        # check if we hit something
        if cannon.outcome == 'X':
            print("\n")
            print("WE HAVE HIT THE SHIP")
            print("\n")
            ship_to_destroy.was_hit = True
            ship_to_destroy.hits.append((row, column))
        else:
            print("WE HAVE MISSED")
            ship_to_destroy.was_hit = False

    # we have found ship, and now we will send hits to destoy it
    # after that new ship to find (currently randomly)
    while ship_to_destroy.was_hit and not ship_to_destroy.destroyed:
        print("WE ARE SHOOTING AT SHIP")
        print(f"REMAINING SHIP {strategy.ships_left}")
        # get the positions around the ship
        possible_moves_around_ship = sea_map.filter_moves(ship_to_destroy.get_moves())

        # check if there is not any hit to make, ship has been destroyed
        if len(possible_moves_around_ship) == 0:

            # here should be checked if avenger ship is destroyed
            # check at length 3 or 5
            if ship_to_destroy.length in [3, 5] and cannon.avenger_available is False:
                possible_avenger = AvengerShip(ship_to_destroy)
                possible_shots = sea_map.filter_moves(possible_avenger.get_moves())

                if not strategy.is_this_ship_destroyed(ship_to_destroy.length):
                    print("Checking if it is avenger")
                    if len(possible_shots) in [6, 9, 10] or len(possible_shots) == 4:
                        row, column = random.choice(possible_shots)
                        cannon.fire_at_position(row, column)
                        sea_map.update_map(cannon.grid_info)
                    else:
                        ship_to_destroy.destroyed = True
                        strategy.remove_destroyed_ship(type_of_ship=ship_to_destroy.length)

                        ship_to_destroy = Ship()
                else:
                    ship_to_destroy = possible_avenger
                    print("\n")
                    print("WE HAVE FOUND THE AVENGER SHIP")
                    print("\n")
            else:
                ship_to_destroy.destroyed = True
                strategy.remove_destroyed_ship(type_of_ship=ship_to_destroy.length)
                print("\n")
                print("WE DESTOYED SHIP")
                print("\n")

                ship_to_destroy = Ship()
        else:
            row, column = random.choice(possible_moves_around_ship)
            cannon.fire_at_position(row, column)
            sea_map.update_map(cannon.grid_info)

            if cannon.outcome == 'X':
                ship_to_destroy.hits.append((row, column))

    num_of_tries = cannon.moveCount
    # map_count = cannon.mapCount


# NOTES
"""

1 iterace 
    mame zamerenou lod ktera neni znicena? 
        ano
            strilime po ni
        ne 
            podivame se jake mame zbyle lode a kde je prostor
            strilime na vybrany prostor
            trefa? 
                ano 
                    - mame zamerenou lod 
                ne  
                    opakujeme hledani 
                

mam 3 nebo 5 lod a avengers neni najita 
    podiovam se jestli mi jeste zbyvaji lode 3 a 5 
        zkontroluji jestli se tam vleze a kam 
            ne - neni avenger
                lod je o daneho rozmeru znicena
            ano - test strela 
                vysledek -
                voda - 
                    pokud je dana delka 5
                        = znicena lod o dane delce
                    pokud 3 a vleze se na obe strany 
                        test strela
                            voda 
                                znicena lod
                            zasah 
                                avenger
                trefa 
                    je avenger

    pokud vsechny 3 a 5 znicene
        je avenger
pokud uz avenger najity 
    znicena lod o dane delce 


"""
