import unittest, os
from dijkstra import Dijkstra
from filereader import Reader
from math import inf

DIRNAME = os.path.dirname(__file__)

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.reader = Reader(os.path.join(DIRNAME, "maps", "testmap1.map"))
        level_data = self.reader.parse_data()
        self.dijkstra = Dijkstra(level_data[2])

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
