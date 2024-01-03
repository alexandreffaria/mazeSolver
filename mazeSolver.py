from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():

    num_rows = 20
    num_cols = 20
    margin = 50
    screen_x = 1000
    screen_y = 1000

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)

    labirinto = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()