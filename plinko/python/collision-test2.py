from pegs import *
from balls import *
from boardfuncs import *

STARTING_DROPx = -0.1
STARTING_DROPy = 0.5

MIN_x, MAX_x = -1,1
MIN_y, MAX_y = -1,1

dt = 0.5


BOARD_DIM = [MIN_x,MAX_x,MIN_y,MAX_y]

testpeg = Peg(0,0,0.25)
PEG_LIST = [testpeg]

testvel = Vector(0,-1)

balldrop = Ball(STARTING_DROPx,STARTING_DROPy,testvel)
newpos = get_new_position(balldrop, testvel, dt,gravity=Vector(0,0))

balldrop.collision_update(newpos, testvel, testpeg)