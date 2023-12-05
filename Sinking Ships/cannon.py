import requests


class Cannon:

    def __init__(self, headers, query_params, api_endpoint):
        self.headers = headers
        self.query_params = query_params
        self.api_endpoint = api_endpoint
        self.grid_info = None
        self.outcome = None
        self.valid_shot = None
        self.avenger_available = False
        self.mapId = None
        self.mapCount = None
        self.moveCount = None
        self.game_finished = None

    def fire_at_position(self, row, col):
        api_fire = f'{self.api_endpoint}{row}/{col}/'
        response_fire = requests.get(url=api_fire, headers=self.headers, params=self.query_params)
        data = response_fire.json()
        self.update_data(data)
        return self.outcome

    def get_current_situation(self):
        response_fire = requests.get(url=self.api_endpoint, headers=self.headers, params=self.query_params)
        data = response_fire.json()
        self.update_data(data)

    def update_data(self, data):
        self.grid_info = data['grid']
        self.outcome = data['cell']
        self.valid_shot = data['result']
        self.avenger_available = data['avengerAvailable']
        self.mapId = data['mapId']
        self.mapCount = data['mapCount']
        self.moveCount = data['moveCount']
        self.game_finished = data['finished']

