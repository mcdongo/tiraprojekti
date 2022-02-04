from heapq import heappop, heappush
from math import inf


class Dijkstra:
    """Luokka, jonka vastuulla on löytää lyhyin reitti
        tietyistä koordinaateista toisiin Dijkstran algoritmin
        avulla.

    attr:
        _map (List): karttadata matriisiesityksenä
        _path_map (List): pitää kirjaa KAIKISTA algoritmin tekemistä
            askelista (tallentaa käytyjen kohteiden koordinaatit (y,x) tuplena)
    """

    def __init__(self, level_map):
        """Metodi, joka toteutetaan kun olio luodaan

        args:
            map (List): karttadata matriisiesityksenä
        """
        self._map = level_map
        self._path_map = []

    def set_map(self, level_map):
        """Metodi, jolla voi asettaa toisen kartan olion
            kartaksi.

        args:
            map (List): karttadata matriisiesityksenä
        """
        self._map = level_map

    def get_map(self):
        """Metodi, joka palauttaa olion nykyisen kartan

        returns:
            _map (List): karttadata matriisiesityksenä
        """
        return self._map

    def get_path_map(self):
        """Metodi, joka palauttaa listan missä on algoritmin tekemät askeleet

        returns:
            _path_map (List): lista, jossa on kaikki sijainnit missä algoritmi on vieraillut
                muotoa (y,x) tupleina.
        """
        return self._path_map

    def solve(self, start, end):
        """Metodi, joka tekee algoritmin ydintoiminnallisuuden,
            eli etsii lyhimmän reitin alkukoordinaateista loppukoordinaatteihin

        args:
            start (tuple): 2-alkioinen tuple (y (int), x (int)),
                missä määritellään reitinhaun alkupiste
            end (tuple): 2-alkionen tuple (y (int), x (int)),
                missä määritellään reitinhaun loppupiste
        returns:
            dist[goal_y][goal_x] (int): tarvittavien askelien määrä
                alkukoordinaateista loppukoordinaatteihin
        """
        start_y, start_x = start
        goal_y, goal_x = end
        heap = []
        dist = [[inf]*len(self._map[0]) for _ in range(len(self._map))]
        dist[start_y][start_x] = 0
        self._completed = [[False]*len(self._map[0])
                           for _ in range(len(self._map))]

        heappush(heap, (start_y, start_x))

        while heap:
            node = heappop(heap)
            if self._completed[node[0]][node[1]]:
                continue
            self._completed[node[0]][node[1]] = True

            # [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_pos = (node[0]+direction[0], node[1]+direction[1])
                tile = self._map[new_pos[0]][new_pos[1]]
                if tile in ('.', 'S'):
                    cur = dist[new_pos[0]][new_pos[1]]
                    new = dist[node[0]][node[1]] + 1
                    self._path_map.append((new_pos[0], new_pos[1]))
                    if new < cur:
                        dist[new_pos[0]][new_pos[1]] = new
                        heappush(heap, (new_pos[0], new_pos[1]))
                else:
                    self._completed[new_pos[0]][new_pos[1]] = True
                if self.check_for_completion(new_pos, (goal_y, goal_x)):
                    heap = None
                    break

        return dist[goal_y][goal_x]

    def check_for_completion(self, cur_pos, end):
        """Metodi, joka tarkistaa onko algoritmi valmis
        katsomalla onko kaikki loppupisteen ympäröivät
        koordinaatit jo algoritmin käsittelemiä

        args:
            cur_pos (tuple): 2-alkionen tuple (y (int), x (int))
                mikä kuvaa algoritmin tämänhetkisen tarkastelun alla
                olevaa sijaintia
            end (tuple): 2-alkioinen tuple (y (int), x(int))
                mikä kuvaa loppupistettä mihin reitti halutaan löytää

        returns:
            all_completed (boolean): True, jos kaikki ympäröivät "solmut"
                on käsitelty, False muuten
        """
        if cur_pos != end:
            return False
        all_completed = True
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (cur_pos[0]+direction[0], cur_pos[1]+direction[1])
            if self._completed[new_pos[0]][new_pos[1]]:
                continue
            all_completed = False
        return all_completed
