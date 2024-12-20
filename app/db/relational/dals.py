import json

class TG_DAL:
    def __init__(self):
        pass

    def _get_api_keys(self, path_to_file):
        dct = json.load(open(f"{path_to_file}/data.json"))

        return dct