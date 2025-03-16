from Window import Point, Line

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self, f_color="black"):
        if self.has_left_wall:
            l_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(l_wall, f_color)
        if self.has_top_wall:
            t_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(t_wall, f_color)
        if self.has_right_wall:
            r_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(r_wall, f_color)
        if self.has_bottom_wall:
            b_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(b_wall, f_color)