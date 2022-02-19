from math import inf
from algorithm_base import PriorityQueue, Algorithm


class JPS(Algorithm):
    """Luokka, joka vastaa JPS-algoritmin toiminnasta.
    Tällä hetkellä JPS ei ole vielä valmis, vaan rungoksi
    on rakennettu A*-algoritmi! Olio perii isäntäolion Algorithm
    ja käyttää sen metodeja sekä moduulin algorithm_base.py
    PriorityQueue-olion.

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
        super().__init__(level_map)

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
        self._path_map = []
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
