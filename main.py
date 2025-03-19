from window import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # Test Maze
    num_rows = 15
    num_cols = 18
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 15)
    maze.solve()

    win.wait_for_close()

main()
