from math import sqrt
from heapq import heappush, heappop


class PriorityQueue:
    """Olio, joka toimii prioriteettijonona molemmille algoritmeille

    attr:
        _elements (heap): Keko, mikä on järjestyy algoritmin määrittelemän
            prioriteetin avulla
    """

    def __init__(self):
        self._elements = []

    def is_empty(self):
        """Metodi, joka palauttaa True, jos keko on tyhjä,
        muuten False"""
        return not self._elements

    def insert(self, pos, priority):
        """Metodi, joka lisää kekoon uuden sijainnin
        ja järjestää sen annetun prioriteetin nojalla

        args:
            priority (Float): arvioitu etäisyys kyseisestä solmusta
                kohdesolmuun
        """
        heappush(self._elements, (priority, pos))

    def empty_queue(self):
        """Metodi, joka tyhjentää prioriteettijonon"""
        self._elements = []

    def get_next(self):
        """Metodi, joka palauttaa seuraavan korkeimman prioriteetin
        koordinaattiparin keosta

        returns:
            Tuple: (y (int) x(int)), seuraavan pisteen koordinaatit
        """
        return heappop(self._elements)[1]


class Algorithm:
    """Isäntäluokka, jonka algoritmit perivät. Sisältää
    metodeja, joita molemmat algoritmit käyttävät.

    attr:
        _map (List): matriisiesitys karttadatasta
        _path_map (List): lista, mikä pitää kirjaa kaikista
            koordinaateista missä algoritmi on vieraillut
    """

    def __init__(self, level_map):
        """Olion konstruktori.

        args:
            level_map (List): karttadata matriisiesityksenä
        """
        self._map = level_map
        self._path_map = []

    def set_map(self, level_map):
        """Metodi, joka asettaa oliolle uuden karttadatan

        args:
            level_map (List): karttadata matriisiesityksenä
        """
        self._map = level_map

    def get_map(self):
        """Metodi, joka palauttaa algoritmin tämänhetkisen
        karttadatan

        returns:
            _map (List): karttadata matriisiesityksenä
        """
        return self._map

    def get_path_map(self):
        """Metodi, joka palauttaa algoritmin läpikäyneet
        koordinaatit

        returns:
            _path_map (List): lista 2-alkioisista tupleista (y (int), x (int))
                mitkä kuvaa algoritmin läpikäyneitä koordinaatteja
        """
        return self.unique_coords(self._path_map)

    def unique_coords(self, path):
        """Metodi, joka vastaanottaa listan koordinaatteja.
        Metodi käy listan läpi ja palauttaa uuden listan, missä
        ei ole duplikaatteja ollenkaan, eli sama koordinaatti ei esiinny
        kahdesti.

        args:
            path (List): Algoritmin käsittelemät koordinaatit
                2-alkioisina tupleina (y (int), x (int))
        returns:
            List: Käsitelty lista, missä ei ole duplikaatteja
        """
        seen = set()
        return [x for x in path if not (x in seen or seen.add(x))]

    def h(self, cur_pos, wanted_pos):
        """Metodi, joka antaa arvion kahden pisteen välisestä etäisyydestä
        ottamatta huomioon mahdollisia esteitä niiden väliltä.

        args:
            cur_pos (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä on vertailun ensimmäinen piste
            wanted_pos (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä on vertailun jälkimmäinen piste

        returns:
            float: näiden kahteen pisteen välille arvioitu etäisyys
        """
        (y1, x1) = cur_pos
        (y2, x2) = wanted_pos

        return sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

    def gather_shortest_path(self, start, end):
        """Metodi, joka palauttaa lyhyimmän reitin alku-
        ja loppupisteen väliltä.

        args:
            start (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä kuvaa lähtöpistettä
            end (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä kuvaa loppupistettä
        returns:
            path (List): lista 2-alkioisia tupleja (y (int), x (int))
                mikä kuvaa lyhyintä reittiä väliltä start-end
        """
        path = []
        path.append(end)
        cur = end

        while self.parent[cur] is not None:
            path.append(self.parent[cur])
            cur = self.parent[cur]

        path.reverse()
        return path
