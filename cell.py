from window import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        l_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        t_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        r_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        b_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall:   
            self._win.draw_line(l_wall)
        else:
            self._win.draw_line(l_wall, f_color="white")
        if self.has_top_wall:
            self._win.draw_line(t_wall)
        else:
            self._win.draw_line(t_wall, f_color="white")
        if self.has_right_wall:
            self._win.draw_line(r_wall)
        else:
            self._win.draw_line(r_wall, f_color="white")
        if self.has_bottom_wall:
            self._win.draw_line(b_wall)
        else:
            self._win.draw_line(b_wall, f_color="white")
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        start_x = self._x1 + (self._x2-self._x1)/2
        start_y = self._y1 + (self._y2-self._y1)/2
        end_x = to_cell._x1 + (to_cell._x2-to_cell._x1)/2
        end_y = to_cell._y1 + (to_cell._y2-to_cell._y1)/2
        path = Line(Point(start_x, start_y), Point(end_x, end_y))
        f_color = "red"
        if undo:
            f_color = "gray"
        self._win.draw_line(path, f_color)