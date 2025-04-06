import json
import os
from scripts.tilemap import tile_map

class MapManager:

    def __init__(self):

        self.json_dict = {}
        self.current_map_id = ''
        self.update_map_dict()

    def update_map_dict(self):
        self.json_dict = {}
        folder_path = "data/onlineMaps"
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.json_dict[data["info"]["id"]] = data

    def getMapPath(self):
        return f"data/onlineMaps/{self.current_map_id}.json"

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
        # source_path = f"data/maps/{self.current_map_id}.json"
        # dest_path = "map.json"

        # # Load map data
        # with open(source_path, 'r') as f:
        #     map_data = json.load(f)

        # map_info = map_data["info"]
        # map_tilemap = map_data["tilemap"]
        # map_offgrid = map_data["offgrid"]

        # # Write selected data to new file
        # with open(dest_path, 'w') as f:
        #     json.dump({'info': map_info, 'tilemap': map_tilemap, 'offgrid': map_offgrid}, f, indent=4)
        map_path = self.getMapPath()
        tile_map.load(map_path)
                

map_manager = MapManager()
