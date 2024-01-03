import unittest
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze1._cells),
            num_cols
        )
        self.assertEqual(
            len(maze1._cells[0]),
            num_rows
        )
    def test_maze_create_cells_not_square(self):
        num_cols = 2
        num_rows = 2
        maze2 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(maze2._cells),
            num_cols
        )
        self.assertEqual(
            len(maze2._cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()
