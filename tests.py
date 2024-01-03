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

    def test_maze_break_entrance_and_exit(self):
        maze = Maze(0, 0, 3, 3, 10, 10)
        maze._break_entrance_and_exit()

        entrance_cell = maze._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)

        exit_cell = maze._cells[maze._num_cols - 1][maze._num_rows - 1]
        self.assertFalse(exit_cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
