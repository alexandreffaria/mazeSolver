import unittest, random
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

    def test_reset_all_cells_visited(self):
        num_rows = 20
        num_cols = 20
        margin = 10
        screen_x = 1000
        screen_y = 1000
        seed = random.randint(0,1000)

        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        
        labirinto = Maze(
        margin, margin, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y,
        None, 
        seed)

        labirinto._break_entrance_and_exit()
        labirinto._break_walls_r(0, 0)
        labirinto._reset_cells_visited()

        for col_cells in labirinto._cells:
            for cell in col_cells:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
