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
        _dijkstra_level (Level): level-olio, missä on Dijkstran algoritmin tuorein karttadata
        _jps_level (Level): level-olio, missä on JPS-algoritmin tuorein karttadata

    """

    def __init__(self, display, dijkstra_level, jps_level, width, height):
        """Metodi, joka toteutetaan, kun olio luodaan

        args:
            display (pygame.display): olio, joka vastaa ikkunasta mille piirretään
            dijkstra_level (Level): level-olio, missä on Dijkstran algoritmin tuoren karttadata
            jps_level (Level): level-olio, missä on JPS-algoritmin tuorein karttadata
            width (int): ikkunan leveys
            height (int): ikkunan korkeus
        """
        self._display = display
        self._dijkstra_level = dijkstra_level
        self._jps_level = jps_level
        self.setup_hud(width, height)

    def setup_hud(self, width, height):
        """Metodi, joka luo tarvittavat oliot tekstin
            ja nappuloiden piirtymiseen ikkunalle

        args:
            width (int): ikkunan leveys
            height (int): ikkunan korkeus
        """
        font = pg.font.SysFont("Caladea", 32)
        button_font = pg.font.SysFont("Caladea", 14)
        left_text = font.render(
            "Dijkstran algoritmi", True, (255, 255, 255))
        right_text = font.render("JPS", True, (255, 255, 255))
        left_text_rect = left_text.get_rect()
        left_text_rect.center = (round(width*0.25), height - 25)
        right_text_rect = right_text.get_rect()
        right_text_rect.center = (round(width*0.75), height - 25)

        self.button = pg.Surface((105, 20))
        self.button.fill((200, 0, 0))
        self.button_text = button_font.render(
            'Vaihda näkymä', 1, (255, 255, 255))
        self.button.blit(self.button_text, (5, 0))
        self.button_rect = self.button.get_rect()
        self.button_rect.center = (round(width*0.07), height - 45)

        self._hud_list = [(left_text, left_text_rect), (right_text, right_text_rect),
                          (self.button, self.button_rect)]

    def render(self):
        """Metodi, joka piirtää kaiken näytölle.
        Metodi hakee Level-oliolta tuoreimman karttadatan ja piirtää pikseli kerrallaan
        jonkin värin jokaista koordinaattia vastaavaa merkkiä vasten.
        Lopuksi piirtää hud-elementit ikkunan alareunaan.
        """
        self._display.fill((0, 0, 0))
        dijkstra_level_map = self._dijkstra_level.get_level_map()
        jps_level_map = self._jps_level.get_level_map()
        self._display.fill(COLORS["@"])
        for i in range(len(dijkstra_level_map)):
            for j in range(len(dijkstra_level_map[i])):
                self._display.set_at((j, i), COLORS[dijkstra_level_map[i][j]])
                self._display.set_at(
                    (j+len(jps_level_map[i]), i), COLORS[jps_level_map[i][j]])

        for hud_object, object_rect in self._hud_list:
            self._display.blit(hud_object, object_rect)

    def check_for_highlight(self, mouse_pos):
        """Metodi, joka tarkistaa onko hiiri nappulan
            sisäpuolella
        args:
            mouse_pos (tuple): 2-alkioinen tuple, hiiren
                koordinaatit (x (int), y (int))
        returns:
            True mikäli ehto täyttyy
            False muuten
        """
        if (mouse_pos[0] > self.button_rect.left and
            mouse_pos[0] < self.button_rect.right and
            mouse_pos[1] > self.button_rect.top and
                mouse_pos[1] < self.button_rect.bottom):
            return True
        return False

    def highlight_button(self, mouse_pos):
        """Metodi, joka vaihtaa nappulan väriä
            mikäli check_for_highlight palauttaa
            True
        args:
            mouse_pos (tuple): 2-alkioinen tuple,
                hiiren koordinaatit (x (int), y (int))
        """
        if self.check_for_highlight(mouse_pos):
            self.button.fill((255, 0, 0))
        else:
            self.button.fill((200, 0, 0))

        self.button.blit(self.button_text, (5, 0))
