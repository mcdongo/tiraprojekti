from math import inf
from algorithm_base import PriorityQueue, Algorithm


class Dijkstra(Algorithm):
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
        super().__init__(level_map)

    def solve(self, start, end):
        """Metodi, joka tekee algoritmin ydintoiminnallisuuden,
            eli etsii lyhimmän reitin alkukoordinaateista loppukoordinaatteihin.
            Algoritmi on ahne, eli pahimmassa mahdollisessa tilanteessa
            se käsittelee koko kartan ennen kuin se on löytänyt lyhyimmän
            reitin alkupisteestä loppupisteeseen.

        args:
            start (tuple): 2-alkioinen tuple (y (int), x (int)),
                missä määritellään reitinhaun alkupiste
            end (tuple): 2-alkionen tuple (y (int), x (int)),
                missä määritellään reitinhaun loppupiste
        returns:
            dist[goal_y][goal_x] (int): tarvittavien askelien määrä
                alkukoordinaateista loppukoordinaatteihin
        """
        self._path_map = []
        queue = PriorityQueue()
        dist = {}
        self.parent = {}
        self.parent[start] = None
        dist[start] = 0
        self._completed = {}

        queue.insert(start, 0)

        while not queue.is_empty():
            node = queue.get_next()
            if node in self._completed:
                continue
            self._completed[node] = True

            for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_pos = (node[0]+direction[0], node[1]+direction[1])
                tile = self._map[new_pos[0]][new_pos[1]]
                if tile in ('.', 'S'):
                    if new_pos not in dist:
                        dist[new_pos] = inf
                    cur = dist[new_pos]
                    new = dist[node] + \
                        self.h(node, new_pos)
                    self._path_map.append(new_pos)
                    if new < cur:
                        dist[new_pos] = new
                        self.parent[new_pos] = (node)
                        queue.insert(new_pos, new)
                if self.check_for_completion(new_pos, end):
                    queue.empty_queue()
                    break

        return dist[end] if end in dist else inf

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
        for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            new_pos = (cur_pos[0]+direction[0], cur_pos[1]+direction[1])
            if new_pos in self._completed:
                continue
            all_completed = False
        return all_completed
