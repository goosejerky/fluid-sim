from pegs import *
from balls import *

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle



def plot_peg(subplot, in_peg):
    
    xpos = in_peg.center_x
    ypos = in_peg.center_y
    rad = in_peg.radius

    subplot.add_patch(Circle((xpos,ypos), rad))



def plot_board(BOARD_DIM,PEG_LIST,ball):
    
    fig = plt.figure()
    board = fig.add_subplot()
    #peg_layer = fig.add_subplot()
    
    # make border
    xmin,xmax,ymin,ymax = BOARD_DIM    
    rect_width = xmax - xmin
    rect_height = ymax - ymin    
    board.add_patch(Rectangle((xmin,ymin), rect_width, rect_height, fill=False))
    
    
    #plot pegs
    for peg in PEG_LIST:
        plot_peg(board, peg)
    
    
    #plt.xlim(xmin,xmax)
    #plt.ylim(ymax,ymax)
    plt.axis('square')
    plt.show()
    
    
    
def get_new_velocity(ball, dt, gravity=Vector(0, -9.8)):
    
    new_velx = ball.velocity.x + gravity.x*dt
    new_vely = ball.velocity.y + gravity.y*dt
    
    return Vector(new_velx,new_vely)



def get_new_position(ball, new_velocity, dt, gravity=Vector(0, -9.8)):
    
    new_posx = ball.xpos + ball.velocity.x*dt + 0.5*gravity.x*(dt**2)
    new_posy = ball.ypos + ball.velocity.y*dt + 0.5*gravity.y*(dt**2)
    
    return Vector(new_posx,new_posy)