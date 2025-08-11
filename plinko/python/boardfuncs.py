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
    
    
    # plot pegs
    for peg in PEG_LIST:
        plot_peg(board, peg)
    
    
    # plot ball position history
    pos_hist = ball.pos_history
    vel_hist = ball.vel_history
    hist_length = ball.history_length
    
    for j in range(hist_length-1):
        current_pos = pos_hist[j]
        current_vel = vel_hist[j]
        
        dx = pos_hist[j+1].x - current_pos.x
        dy = pos_hist[j+1].y - current_pos.y
        print(dx,dy)
        
        plt.arrow(current_pos.x,current_pos.y, dx, dy, width=0.02)
    
    
    
    
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