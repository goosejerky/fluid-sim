from pegs import *
from balls import *
from boardfuncs import *

STARTING_DROPx = 0
STARTING_DROPy = 1

MIN_x, MAX_x = -1,1
MIN_y, MAX_y = -1,1

dt = 0.1


BOARD_DIM = [MIN_x,MAX_x,MIN_y,MAX_y]

testpeg = Peg(0,0,0.25)
PEG_LIST = [testpeg]



balldrop = Ball(STARTING_DROPx,STARTING_DROPy)

for timestep in range(5):
    
    newvel = get_new_velocity(balldrop, dt)
    newpos = get_new_position(balldrop, newvel, dt)
    
    balldrop.update_position(newpos, newvel)

print(balldrop.pos_history)
print(balldrop.vel_history)


plot_board(BOARD_DIM,PEG_LIST,balldrop)