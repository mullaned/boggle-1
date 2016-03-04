import unittest
from string import ascii_uppercase

import boggle


class test_boggle(unittest.TestCase):
    def test_can_create_an_empty_grid(self):
        grid = boggle.make_grid(0, 0)
        self.assertEquals(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        grid = boggle.make_grid(2, 3)
        self.assertEquals(len(grid), 6)

    def test_grid_coordinates(self):
        grid = boggle.make_grid(2, 2)
        self.assertTrue((0,0) in grid)
        self.assertTrue((0,1) in grid)
        self.assertTrue((1,0) in grid)
        self.assertTrue((1,1) in grid)

    def test_grid_is_filled_with_letters(self):
        grid = boggle.make_grid(2, 3)
        for L in grid.values():
            self.assertTrue(L in ascii_uppercase)

    def test_neighbours_of_a_position(self):
        neighbours = boggle.neighbours_of_position((1, 2))
        self.assertTrue((0,1) in neighbours)
        self.assertTrue((0,2) in neighbours)
        self.assertTrue((0,3) in neighbours)
        self.assertTrue((1,1) in neighbours)
        self.assertTrue((1,3) in neighbours)
        self.assertTrue((2,1) in neighbours)
        self.assertTrue((2,2) in neighbours)
        self.assertTrue((2,3) in neighbours)

    def test_all_neighbours(self):
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.get_neighbours(grid)
        self.assertEquals(len(neighbours), len(grid))
        self.assertListEqual(sorted(neighbours[(0, 0)]), sorted([(0, 1), (1, 1), (1, 0)]))

    def test_search(self):
        grid = boggle.make_grid(2, 2)
        words = boggle.search(grid)
        self.assertEquals(len(words), 64)
        # self.assertEquals(len(words), len(set(words)))
