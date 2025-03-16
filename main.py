from window import *
from cell import Cell

def main():
    win = Window(800, 600)
    # Test Cells
    cell1 = Cell(10,100, 10, 100, win)
    cell1.draw()
        
    cell2 = Cell(200,300, 300, 400, win)
    cell2.has_right_wall = False
    cell2.draw()
    
    win.wait_for_close()

main()
