import unittest
import os
from random import randrange
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
        distance = round(self.dijkstra.solve((1, 1), (1, 8)), 4)

        self.assertEqual(distance, 9.4853)

    def test_minimum_distance2(self):
        distance = round(self.dijkstra.solve((1, 8), (5, 1)), 4)

        self.assertEqual(distance, 8.6569)

    def test_minimum_distance3(self):
        distance = round(self.dijkstra.solve((5, 8), (1, 8)), 4)

        self.assertEqual(distance, 6.2426)

    def test_distance_not_working_with_wrong_coordinates(self):
        distance = self.dijkstra.solve((1, 1), (1, 4))

        self.assertEqual(distance, inf)

    def test_working_path1(self):
        self.dijkstra.solve((1, 1), (1, 3))
        path = self.dijkstra.gather_shortest_path((1, 1), (1, 3))
        shortest_path = [(1, 1), (1, 2), (1, 3)]

        self.assertEqual(shortest_path, path)

    def test_working_path2(self):
        self.dijkstra.solve((5, 8), (5, 1))
        path = self.dijkstra.gather_shortest_path((5, 8), (5, 1))
        shortest_path = [(5, 8), (5, 7), (5, 6), (4, 5),
                         (4, 4), (4, 3), (5, 2), (5, 1)]

        self.assertEqual(path, shortest_path)
