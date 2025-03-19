from cell import *
from window import *
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_celss_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for row in range(self._num_rows)] for col in range(self._num_cols)]

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if self._num_cols == 0 or self._num_rows == 0: 
            return
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_right_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visit = []
            # left cell
            if i > 0 and not self._cells[i-1][j].visited:
                visit.append((i-1,j))
            # right cell
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                visit.append((i+1,j))
            # top cell
            if j > 0 and not self._cells[i][j-1].visited:
                visit.append((i,j-1))
            # bottom cell
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                visit.append((i,j+1))

            if len(visit) == 0:
                self._draw_cell(i, j)
                return
            
            selected = visit[random.randrange(len(visit))]
            # left cell
            if selected[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # right cell
            if selected[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # top cell
            if selected[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            # bottom cell
            if selected[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._break_walls_r(selected[0], selected[1])

    def _reset_celss_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        # left
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            res = self._solve_r(i-1, j)
            if res:
                return res
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        # top
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            res = self._solve_r(i, j-1)
            if res:
                return res
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        # right
        if i < self._num_cols - 1 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            res = self._solve_r(i+1, j)
            if res:
                return res
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        # bottom
        if j < self._num_rows - 1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            res = self._solve_r(i, j+1)
            if res:
                return res
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        return False
    
