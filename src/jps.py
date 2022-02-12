from heapq import heappop, heappush
from math import inf, sqrt


class PriorityQueue:
    """Olio, joka toimii prioriteettijonona JPS-algoritmille

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

    def get_next(self):
        """Metodi, joka palauttaa seuraavan korkeimman prioriteetin
        koordinaattiparin keosta

        returns:
            Tuple: (y (int) x(int)), seuraavan pisteen koordinaatit
        """
        return heappop(self._elements)[1]


class JPS:
    """Luokka, joka vastaa JPS-algoritmin toiminnasta.
    Tällä hetkellä JPS ei ole vielä valmis, vaan rungoksi
    on rakennettu A*-algoritmi!

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
        return self._path_map

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

    def solve(self, start, end):
        """Algoritmin ydintoiminnallisuus. Tällä hetkellä ei vielä JPS,
        vaan A*!

        args:
            start (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä kuvaa lähtöpistettä
            end (Tuple): 2-alkioinen tuple (y (int), x (int))
                mikä kuvaa loppupistettä

        returns:
            float: etäisyys haluttuun pisteeseen, mikäli siihen on
                mahdollista kulkea
            inf: muuten
        """
        queue = PriorityQueue()
        queue.insert(start, 0)
        self.parent = {}
        self.parent[start] = None

        dist = {}
        dist[start] = 0

        while not queue.is_empty():
            cur_pos = queue.get_next()

            if cur_pos == end:
                break

            for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                              (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_pos = (cur_pos[0] + direction[0],
                           cur_pos[1] + direction[1])

                tile = self._map[new_pos[0]][new_pos[1]]
                if tile in ('.', 'S'):
                    if new_pos not in dist:
                        dist[new_pos] = inf
                    self._path_map.append(new_pos)
                    cur = dist[new_pos]
                    new = dist[cur_pos] + self.h(cur_pos, new_pos)
                    if new < cur:
                        dist[new_pos] = new
                        priority = new + self.h(new_pos, end)
                        queue.insert(new_pos, priority)
                        self.parent[new_pos] = cur_pos

        return dist[end] if end in dist else inf

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

        while self.parent[cur] != None:
            path.append(self.parent[cur])
            cur = self.parent[cur]
            if cur == start:
                break

        path.reverse()
        return path
