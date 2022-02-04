import pygame as pg


class Clock:
    """Luokka, joka vastaa ajankulusta visualisoinnissa käyttäen pygame-kirjastoa

    attr: _clock (pygame.time.Clock)
    """

    def __init__(self):
        """Metodi, joka toteutetaan, kun olio luodaan
        """
        self._clock = pg.time.Clock()

    def tick(self, fps):
        """Metodi, joka määrittää visualisoinnin virkistystaajuuden

        args:
            fps (int): Kuinka monta kertaa visualisoinnin halutaan päivittyvän sekunnissa
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Metodi, joka paluttaa kuinka monta kertaa visualisointia on jo päivitetty

        returns:
            pg.time.get_ticks() (int): päivityskertojen lukumäärä siitä hetkestä,
            kun ohjelma käynnistettiin
        """
        return pg.time.get_ticks()
