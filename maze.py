from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_y
        self.cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(num_cols):
            for j in range(num_rows):
                self.cells.append(Cell())
        for cell in self._cells:
            self._draw_cell(cell, i, j)

    def _draw_cell(self, i, j):
        pass




    def _animate(self):
        pass