class Level:
    def __init__(self,level_map):
        self._level_map = level_map

    def get_level_map(self):
        return self._level_map

    def get_coordinate(self,y,x):
        return self._level_map[y][x]

    def edit_coordinate(self,y,x,value):
        self._level_map[y][x] = value