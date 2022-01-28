import pygame as pg
from random import randint

class Loop:
    def __init__(self,level,renderer,event_queue,clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pg.QUIT:
                return False

    def _render(self):
        self._renderer.render()
        pg.display.update()

    def set_dijkstra_path_map(self,path):
        self._dijkstra_path_map = path

    def _exhaust_dijkstra_path(self):
        if len(self._dijkstra_path_map) > 0:
            return self._dijkstra_path_map.pop(0)

    def _show_dijkstra_progress(self):
        for i in range(500):
            new_spot = self._exhaust_dijkstra_path()
            if new_spot:
                self._level.edit_coordinate(new_spot[0],new_spot[1],"O")

    def loop(self):
        while True:
            if self._handle_events() is False:
                break

            self._show_dijkstra_progress()
            self._render()
            self._clock.tick(60)