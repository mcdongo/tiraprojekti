import unittest
from dijkstra import Dijkstra
from math import inf

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        level_map = ["@@@@@@@@@@",
                     "@...WWW..@",
                     "@..TW.W..@",
                     "@T..T....@",
                     "@.T....TT@",
                     "@...TT...@",
                     "@@@@@@@@@@"]
        temp = []
        for y in range(len(level_map)):
            temp.append(list(level_map[y]))
        level_map = temp
        self.dijkstra = Dijkstra(level_map)

    def test_minimum_distance1(self):
        distance = self.dijkstra.solve((1,1),(1,8))

        self.assertEqual(distance,13)

    def test_minimum_distance2(self):
        distance = self.dijkstra.solve((1,8),(5,1))

        self.assertEqual(distance,11)
    
    def test_minimum_distance3(self):
        distance = self.dijkstra.solve((5,8),(1,8))

        self.assertEqual(distance,8)

    def test_distance_not_working_with_wrong_coordinates(self):
        distance = self.dijkstra.solve((1,1),(1,4))
        
        self.assertEqual(distance, inf)
