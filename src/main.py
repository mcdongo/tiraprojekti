from filereader import Reader
from renderer import Renderer
from level import Level
from event_queue import EventQueue
from loop import Loop
from clock import Clock
from dijkstra import Dijkstra
import os
import pygame as pg


DIRNAME = os.path.dirname(__file__)


class Main:
    def __init__(self, name):
        self.load_modules(name)
        '''print(self.level.get_coordinate(66,83))
        dijkstra_val = self.dijkstra.solve((447,420),(104,64))
        print(f"Koordinaateista (y,x) (69,83) koordinaatteihin (447,420) kuluu Dijkstran algoritmin avulla {dijkstra_val} askelta.")
        path_map = self.dijkstra.get_path_map()
        self.loop.set_dijkstra_path_map(path_map)'''
        self.loop.loop()

    def load_reader(self, name):
        self.reader = Reader(os.path.join(DIRNAME, "maps", name))

    def get_level_data(self):
        return self.reader.parse_data()

    def solve_dijkstra(self, start, goal):
        print(self.dijkstra.solve(start, goal))

    def load_modules(self, name):
        pg.init()
        pg.font.init()
        self.load_reader(name)
        level_data = self.get_level_data()
        self.level = Level(level_data[2])
        self.event_queue = EventQueue()
        self.clock = Clock()
        self.display = pg.display.set_mode((level_data[1], level_data[0]))
        self.renderer = Renderer(
            self.display, self.level, level_data[1], level_data[0])
        self.loop = Loop(self.level, self.renderer,
                         self.event_queue, self.clock)
        self.dijkstra = Dijkstra(self.level.get_level_map())


if __name__ == "__main__":
    '''map_list = os.listdir(os.path.join(DIRNAME,"maps"))
    input("Tervetuloa, valitse jokin seuraavista kartoista:")
    for map in map_list:
        print(map)
    desired_map = ""
    while True:
        desired_map = input("Anna kartan nimi: ")
        if desired_map in map_list:
            break
        print(f"{desired_map} ei ole olemassa.")'''
    main = Main("battleground.map")
