import pygame as pg
from random import randint
from dijkstra import Dijkstra

class Loop:
    def __init__(self,level,renderer,event_queue,clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.pos_list = [(),()]
        self.pos_index = 0
        self.dijkstra = Dijkstra(self._level.get_level_map())
        self._dijkstra_path_map = []

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.MOUSEBUTTONUP:
                self._get_mouse_coordinates()
                

    def _get_mouse_coordinates(self):
        if self._dijkstra_path_map == []:
            self.pos_list[self.pos_index] = (pg.mouse.get_pos()[1],pg.mouse.get_pos()[0])
            if self.pos_index == 1:
                print(f"Koordinaateista {self.pos_list[0]} -> {self.pos_list[1]} menee Dijkstran algoritmilla ",end="")
                print(self.dijkstra.solve(self.pos_list[0],self.pos_list[1]),"askelta.")
                self.set_dijkstra_path_map(self.dijkstra.get_path_map())
            self.pos_index = abs(self.pos_index-1)


    def _render(self):
        self._renderer.render()
        pg.display.update()

    def set_dijkstra_path_map(self,path):
        self._dijkstra_path_map = path

    def _exhaust_dijkstra_path(self):
        if len(self._dijkstra_path_map) > 0:
            return self._dijkstra_path_map.pop(0)

    def _show_dijkstra_progress(self):
        for i in range(50):
            new_spot = self._exhaust_dijkstra_path()
            if new_spot:
                self._level.edit_coordinate(new_spot[0],new_spot[1],"O")

    def loop(self):
        while True:
            if self._handle_events() is False:
                break
            #if self._dijkstra_path_map == []:
            #    print(pg.mouse.get_pos())
            self._show_dijkstra_progress()
            self._render()
            self._clock.tick(60)