import json
import os

class MapManager:

    def __init__(self):

        self.json_dict = {}
        self.current_map_id = ""
        self.update_map_dict()

    def update_map_dict(self):

        self.json_dict = {}
        folder_path = "data/maps"
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.json_dict[data["info"]["id"]] = data

    def getMapDict(self):
        self.update_map_dict()
        return self.json_dict

    def setMap(self, id):
        self.current_map_id = id

    def getMapInfo(self, id):
        return self.json_dict[id]["info"]
        
    def getMapJson(self, id):
        return self.json_dict[id]

    def loadMap(self):
        pass

map_manager = MapManager()
