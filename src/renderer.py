import pygame as pg

COLORS = {"W": (0, 0, 255),
          "T": (0, 100, 0),
          "@": (0, 0, 0),
          ".": (255, 255, 255),
          "S": (0, 0, 150),
          "O": (255, 125, 0)}


class Renderer:
    """Luokka, jonka vastuulla on piirtää visualisointi näytölle

    attr:
        _display (pygame.display): olio, joka vastaa ikkunasta mille piirretään
        _level (Level): level-olio, missä on tuorein karttadata

    """

    def __init__(self, display, level, width, height):
        """Metodi, joka toteutetaan, kun olio luodaan

        args:
            display (pygame.display): olio, joka vastaa ikkunasta mille piirretään
            level (Level): level-olio, missä on tuoren karttadata
            width (int): ikkunan leveys
            height (int): ikkunan korkeus
        """
        self._display = display
        self._level = level
        self.setup_text(width, height)

    def setup_text(self, width, height):
        """Metodi, joka luo tarvittavat oliot tekstin piirtymiseen ikkunalle

        args:
            width (int): ikkunan leveys
            height (int): ikkunan korkeus
        """
        font = pg.font.SysFont("Comic Sans MS", 32)
        self.left_text = font.render(
            "Dijkstran algoritmi", True, (255, 255, 255))
        self.right_text = font.render("JPS", True, (255, 255, 255))
        self.left_text_rect = self.left_text.get_rect()
        self.left_text_rect.center = (round(width*0.25), height - 25)
        self.right_text_rect = self.right_text.get_rect()
        self.right_text_rect.center = (round(width*0.75), height - 25)

    def render(self):
        """Metodi, joka piirtää kaiken näytölle.
        Metodi hakee Level-oliolta tuoreimman karttadatan ja piirtää pikseli kerrallaan
        jonkin värin jokaista koordinaattia vastaavaa merkkiä vasten.
        Lopuksi piirtää tekstit ikkunan alareunaan.
        """
        self._display.fill((0, 0, 0))
        level_map = self._level.get_level_map()
        self._display.fill(COLORS["@"])
        for i in range(len(level_map)):
            for j in range(len(level_map[i])):
                self._display.set_at((j, i), COLORS[level_map[i][j]])
                self._display.set_at(
                    (j+len(level_map[i]), i), COLORS[level_map[i][j]])
        self._display.blit(self.left_text, self.left_text_rect)
        self._display.blit(self.right_text, self.right_text_rect)
