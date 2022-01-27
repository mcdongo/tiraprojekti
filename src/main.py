from multiprocessing import Event
from filereader import Reader
from renderer import Renderer
from level import Level
from event_queue import EventQueue
from loop import Loop
from clock import Clock
import os
import pygame as pg


DIRNAME = os.path.dirname(__file__)

class Main:
    def __init__(self,name):
        self.reader = Reader(os.path.join(DIRNAME,"maps",name))
        level_data = self.get_level_data()
        self.display = pg.display.set_mode((level_data[1],level_data[0]))
        pg.init()
        pg.font.init()
        self.level = Level(level_data[2])
        self.event_queue = EventQueue
        self.clock = Clock()
        self.renderer = Renderer(self.display,level_data[2],level_data[1],level_data[0])
        self.loop = Loop(self.level,self.renderer,self.event_queue,self.clock)
        self.loop.loop()

    def get_level_data(self):
        return self.reader.parse_data()

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
    main = Main("hillsofglory.map")
