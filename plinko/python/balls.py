class Vector:
    def __init__(self,x,y,origin_x=0,origin_y=0):
        
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.x = x
        self.y = y
        
    def __str__(self):
        
        outstr = "Vector({0},{1},{2},{3})".format(self.x,self.y,self.origin_x,self.origin_y)
        return outstr
    
    def __repr__(self):
        
        outstr = "Vector({0},{1},{2},{3})".format(self.x,self.y,self.origin_x,self.origin_y)
        return outstr



class Ball:
    def __init__(self,xpos,ypos, starting_velocity=Vector(0,0)):
        
        self.xpos = xpos
        self.ypos = ypos
        
        self.velocity = starting_velocity
        
        self.history = [Vector(0,0)]
        
        
    def update_position(self,vel_vector):
        
        self.xpos += vel_vector.x
        self.ypos += vel_vector.y
        
        self.history.append(vel_vector)