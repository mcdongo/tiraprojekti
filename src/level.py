class Level:
    def __init__(self,level_map):
        self.level_map = level_map

    def get_level_map(self):
        return self.level_map

    def get_coordinate(self,x,y):
        return self.level_map[y][x]