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
        
        self.pos_history = [Vector(xpos,ypos)]
        self.vel_history = [starting_velocity]
        
        
    def update_position(self,pos_vector,vel_vector):
        
        self.xpos = pos_vector.x
        self.ypos = pos_vector.y
        
        self.velocity = vel_vector
        
        self.pos_history.append(pos_vector)
        self.vel_history.append(vel_vector)