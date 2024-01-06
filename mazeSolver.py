from graphics import Window, Point, Line
from cell import Cell
from maze import Maze
import random, argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='', help="Give me the model to solve: 'd' for Depth or 'b' for Breadth")

    num_rows = 20
    num_cols = 20
    margin = 10
    screen_x = 1000
    screen_y = 1000
    seed = random.randint(0,1000)

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)

    labirinto = Maze(
        margin, margin, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y, 
        win,
        seed)

    labirinto._break_entrance_and_exit()
    labirinto._break_walls_r(0, 0)
    labirinto._reset_cells_visited()

    labirinto.solve("b")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()