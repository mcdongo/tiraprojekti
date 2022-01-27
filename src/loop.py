import pygame as pg

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

    def loop(self):
        while True:
            if self._handle_events() is False:
                break
            self._render()
            self._clock.tick(60)