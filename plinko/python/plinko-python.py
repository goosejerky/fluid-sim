from pegs import *
from balls import *
from boardfuncs import *

STARTING_DROPx = 0
STARTING_DROPy = 1

MIN_x, MAX_x = -1,1
MIN_y, MAX_y = -1,1
BOARD_DIM = [MIN_x,MAX_x,MIN_y,MAX_y]


testpeg = Peg(0,0,0.25)
PEG_LIST = [testpeg]


balldrop = Ball(STARTING_DROPx,STARTING_DROPy)



plot_board(BOARD_DIM,PEG_LIST)