import pygame as pg
from random import randint
from dijkstra import Dijkstra

class Loop:
    """Luokka, joka vastaa kaikesta sovelluslogiikasta visualisoinnin aikana
    
    attr:
        _level (Level): olio, jolla on tuorein karttadata
        _renderer (Renderer): olio, joka vastaa näytölle piirtämisestä
        _event_queue (EventQueue): olio, joka vastaanottaa käyttäjän
            syötteet sovelluksen käytön aikana (hiiren klikkaukset)
        _clock (Clock): olio, joka vastaa ajankulusta ja ruudun
            päivittämisestä visualisoinnin aikana
        pos_list (List): Lista, joka tallentaa halutut alku-
            ja loppukoordinaatit algoritmin reitinhakua varten.
            Listassa on kaksi tyhjää tuple-alkiota, jotka ovat
            muotoa (y (int), x (int)).
        pos_index (int): luku, joka pitää kirjaa siitä tallennetaanko
            seuraavaksi alku- vai loppukoordinaattien sijainti
        dijkstra (Dijkstra): olio, jossa on algoritmin toiminnallisuus
        _dijkstra_path_map (List): lista, missä on kaikki algoritmin
            vieraillut koordinaatit 2-alkioisina tupleina (y (int), x(int))
    """
    def __init__(self,level,renderer,event_queue,clock):
        """Metodi, joka toteutetaan, kun olio luodaan.

        args:
            level (Level): olio, joka vastaa karttadatasta
            renderer (Renderer): olio, joka vastaa näytölle piirtämisestä
            event_queue (EventQueue): Olio, joka vastaa käyttäjän syötteistä
            clock (Clock): olio, joka vastaa ajankulusta
        """
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.pos_list = [(),()]
        self.pos_index = 0
        self.dijkstra = Dijkstra(self._level.get_level_map())
        self._dijkstra_path_map = []

    def _handle_events(self):
        """Metodi, joka ottaa vastaan käyttäjän syötteet
        """
        for event in self._event_queue.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.MOUSEBUTTONDOWN:
                self._get_mouse_coordinates()
                

    def _get_mouse_coordinates(self):
        """Metodi, joka tallentaa halutut koordinaatit
        hiiren klikkauksesta oliolle."""
        if self._dijkstra_path_map == []:
            self.pos_list[self.pos_index] = (pg.mouse.get_pos()[1],pg.mouse.get_pos()[0])
            if self.pos_index == 1:
                print(f"Koordinaateista {self.pos_list[0]} -> {self.pos_list[1]} menee Dijkstran algoritmilla ",end="")
                print(self.dijkstra.solve(self.pos_list[0],self.pos_list[1]),"askelta.")
                self.set_dijkstra_path_map(self.dijkstra.get_path_map())
            self.pos_index = abs(self.pos_index-1)


    def _render(self):
        """Metodi, joka kutsuu Renderer-oliota piirtämään ikkunaan
        ja Pygamen display-oliota päivittämään ikkunan sisältö"""
        self._renderer.render()
        pg.display.update()

    def set_dijkstra_path_map(self,path):
        """Metodi, joka tallentaa Dijkstran algoritmin läpikäyneet
        solmut oliolle
        args:
            path (List): lista 2-alkioisia tupleja (y (int), x (int))
        """
        self._dijkstra_path_map = path

    def _exhaust_dijkstra_path(self):
        """Metodi, joka ottaa algoritmin polusta seuraavan alkion ja palauttaa sen

        returns:
            _dijkstra_path_map.pop(0) (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikäli listassa on vielä alkioita, muuten None
        """
        if len(self._dijkstra_path_map) > 0:
            return self._dijkstra_path_map.pop(0)

    def _show_dijkstra_progress(self):
        """Metodi, joka päivittää Level-olion karttadataa algoritmin käymän polun
        tietojen perusteella.
        """
        for i in range(1000):
            new_spot = self._exhaust_dijkstra_path()
            if new_spot:
                self._level.edit_coordinate(new_spot[0],new_spot[1],"O")

    def loop(self):
        """Metodi, joka pyörittää visualisointia. Loputon silmukka,
        jonka sisällä kaikki tarpeelliset päivitykset ja
        metodikutsut tapahtuvat.
        """
        while True:
            if self._handle_events() is False:
                break
            #if self._dijkstra_path_map == []:
            #    print(pg.mouse.get_pos())
            self._show_dijkstra_progress()
            self._render()
            self._clock.tick(60)