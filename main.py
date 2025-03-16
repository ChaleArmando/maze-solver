from Window import *

def main():
    win = Window(800, 600)
    # Test Lines
    l1 = Line(Point(1,2), Point(50, 90))
    win.draw_line(l1, "blue")
    l2 = Line(Point(92, 156), Point(300, 340))
    win.draw_line(l2, "red")
    win.wait_for_close()

main()
