class Vector:
    def __init__(self,end_x,end_y,start_x=0,start_y=0):
        
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y



class Ball:
    def __init__(self,xpos,ypos, starting_velocity=Vector(0,0)):
        
        self.xpos = xpos
        self.ypos = ypos
        
        self.history = [Vector(0,0)]
        
    def update_position(dt)