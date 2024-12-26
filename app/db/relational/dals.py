import json

from db.relational.scheme import TgChannel

class TG_DAL:
    def __init__(self, path_to_folder: str):
        self.path = path_to_folder

    def get_api_keys(self):
        file = "api.json"
        dct = json.load(open(f"{self.path}/{file}"))

        return dct
    
    def get_tg_channels(self):
        file = "tg_channels.json"
        dct = json.load(open(f"{self.path}/{file}"))

        return [TgChannel(**d) for d in dct]
