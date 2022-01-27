import pygame as pg

class EventQueue:
    def get():
        return pg.event.get()