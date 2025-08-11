from pegs import *
from balls import *
from boardfuncs import *

STARTING_DROPx = 0
STARTING_DROPy = 1

MIN_x, MAX_x = -1,1
MIN_y, MAX_y = -1,1

dt = 0.5


BOARD_DIM = [MIN_x,MAX_x,MIN_y,MAX_y]

testpeg = Peg(0,0,0.25)
PEG_LIST = [testpeg]

testvel = Vector(0,-1)

balldrop = Ball(STARTING_DROPx,STARTING_DROPy,testvel)

for j in range(3):
    newpos = get_new_position(balldrop, testvel, dt,gravity=Vector(0,0))
    result = testpeg.pt_inside(newpos.x, newpos.y)
    #print("position:",result, newpos)
    balldrop.update_position(newpos, testvel)
    
    if not result:
        #colvect = pos_collision(balldrop.current_pos() , testvel, testpeg)
        
        start_pos_vector=balldrop.current_pos()
        vel_vector = testvel
        peg = testpeg
        searchsize=0.01
        
        vel_norm = vel_vector.normal()
        search_vect = vel_norm.scalar_mult(searchsize)
        
        testpt = start_pos_vector
        search_cutoff = int(vel_vector.get_size() / searchsize)
        numsteps = 0
        for k in range(search_cutoff):
            testpt = testpt.vect_add(search_vect)
            numsteps += 1
            if peg.pt_inside(testpt.x,testpt.y):
                print(testpt,numsteps)
                break
            
        new_size = numsteps * vel_vector.get_size()
        col_vect = vel_vector.scalar_mult(new_size)
        
        
        print(col_vect)
    






plot_board(BOARD_DIM,PEG_LIST,balldrop)