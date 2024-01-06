from cell import Cell
from time import sleep
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed


    def _create_cells(self):
        
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if not self._win:
            return

        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self):
        if not self._win:
            return
        
        self._win.redraw()
        sleep(.005)

    def _break_entrance_and_exit(self):
       
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        # mark the current cell at (i, j) as visited
        self._cells[i][j].visited = True

        # create a list of possible movements (in our case, to the top, right, bottom, and left cells)
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        # shuffle the directions to ensure a random path each time
        random.shuffle(directions)

        # check each direction
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy

            # checks if the new cell is valid (within the grid and not visited yet)
            if (0 <= new_i < len(self._cells)) and (0 <= new_j < len(self._cells[i])) and not self._cells[new_i][new_j].visited:
                # knock down the wall to the new cell
                self._knock_down_wall(i, j, (dx, dy))

                # recursively call the function for the new cell
                self._break_walls_r(new_i, new_j)

    def _knock_down_wall(self, i, j, direction):
        """
        Knock down wall between current cell and adjacent one in given direction.
        """
        dx, dy = direction
        cell = self._cells[i][j]
        other_cell = self._cells[i + dx][j + dy]

        if dx == -1:   # moving left
            cell.has_left_wall = False
            other_cell.has_right_wall = False
        elif dx == 1:  # moving right
            cell.has_right_wall = False
            other_cell.has_left_wall = False
        elif dy == -1: # moving up
            cell.has_top_wall = False
            other_cell.has_bottom_wall = False
        elif dy == 1:  # moving down
            cell.has_bottom_wall = False
            other_cell.has_top_wall = False

        # After knocking down the walls, redraw the cells
        self._draw_cell(i, j)
        self._draw_cell(i + dx, j + dy)

    def _reset_cells_visited(self):
        for cell_row in self._cells:
            for cell in cell_row:
                cell.visited = False
