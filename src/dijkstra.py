from heapq import heapify, heappop, heappush
from math import inf

class Dijkstra:
    def __init__(self,map):
        self._map = map
        self._path_map = []

    def set_map(self,map):
        self._map = map

    def get_map(self):
        return self._map

    def get_path_map(self):
        return self._path_map

    def solve(self,start,end):
        start_y,start_x = start
        goal_y,goal_x = end
        heap = []
        dist = [[inf]*len(self._map[0]) for _ in range(len(self._map))]
        dist[start_y][start_x] = 0
        self._completed = [[False]*len(self._map[0]) for _ in range(len(self._map))]

        heappush(heap, (start_y,start_x))

        while heap:
            node = heappop(heap)
            if self._completed[node[0]][node[1]]:
                continue
            self._completed[node[0]][node[1]] = True

            for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_pos = (node[0]+direction[0],node[1]+direction[1])
                tile = self._map[new_pos[0]][new_pos[1]]
                if tile == "." or tile == "S":
                    cur = dist[new_pos[0]][new_pos[1]]
                    new = dist[node[0]][node[1]] + 1
                    self._path_map.append((new_pos[0],new_pos[1]))
                    if new < cur:
                        dist[new_pos[0]][new_pos[1]] = new
                        heappush(heap, (new_pos[0],new_pos[1]))
                    if self.check_for_completion(new_pos,(goal_y,goal_x)):
                        heap = None
                        break
                else:
                    self._completed[new_pos[0]][new_pos[1]] = True

        return dist[goal_y][goal_x]

    def check_for_completion(self,cur_pos,end):
        if cur_pos != end:
            return False
        all_completed = True
        for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_pos = (cur_pos[0]+direction[0],cur_pos[1]+direction[1])
            if self._completed[new_pos[0]][new_pos[1]]:
                continue
            all_completed = False
        return all_completed
        