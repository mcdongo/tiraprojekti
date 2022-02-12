from heapq import heappop, heappush
from math import inf, sqrt

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return not self._elements

    def insert(self, pos, priority):
        heappush(self._elements, (priority, pos))

    def get_next(self):
        return heappop(self._elements)[1]



class JPS:
    def __init__(self, level_map):
        self._map = level_map
        self._path_map = []

    def set_map(self, level_map):
        self._map = level_map

    def get_map(self):
        return self._map

    def get_path_map(self):
        return self._path_map

    def h(self, cur_pos, wanted_pos):
        (y1, x1) = cur_pos
        (y2, x2) = wanted_pos

        return sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

    def solve(self, start, end):
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

