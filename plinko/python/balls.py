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
    
    def scalar_mult(self, scalar):
        
        newx = scalar*self.x
        newy = scalar*self.y
        outvect = Vector(newx, newy,self.origin_x,self.origin_y)
        return outvect
    
    def vect_add(self, vector):
        newx = self.x + vector.x
        newy = self.y + vector.y
        outvect = Vector(newx, newy,self.origin_x,self.origin_y)
        return outvect
    
    def get_size(self):
        
        xdiff = (self.origin_x - self.x)**2
        ydiff = (self.origin_y - self.y)**2
        size = (xdiff + ydiff)**0.5
        return size
    
    def normal(self):
        
        size = self.get_size()
        outvect = self.scalar_mult(1/size)
        return outvect



class Ball:
    def __init__(self,xpos,ypos, starting_velocity=Vector(0,0)):
        
        self.xpos = xpos
        self.ypos = ypos
        
        self.velocity = starting_velocity
        
        self.pos_history = [Vector(xpos,ypos)]
        self.vel_history = [starting_velocity]
        self.history_length = 0
        
        
    def update_position(self,pos_vector,vel_vector):
        
        self.xpos = pos_vector.x
        self.ypos = pos_vector.y
        
        self.velocity = vel_vector
        
        self.pos_history.append(pos_vector)
        self.vel_history.append(vel_vector)
        self.history_length += 1
        
    def current_pos(self):
        
        outvect = Vector(self.xpos,self.ypos)
        return outvect
    
    def collision_update(self,newpos_vect,newvel_vect,peg):
        
        does_collide = peg.pt_inside(newpos_vect.x,newpos_vect.y)
        if not does_collide:
            return
        else:
            s_start = self.current_pos()
            v_start = self.velocity
            #print(s_start,v_start)
            s_col = pos_collision(self.current_pos(), self.velocity, peg)
            print(s_col)
            
            
def pos_collision(start_pos_vector, vel_vector, peg, searchsize=0.01):
     
    vel_norm = vel_vector.normal()
    search_vect = vel_norm.scalar_mult(searchsize)
    
    testpt = start_pos_vector
    search_cutoff = int(vel_vector.get_size() / searchsize)
    numsteps = 0
    for k in range(search_cutoff):
        testpt = testpt.vect_add(search_vect)
        numsteps += 1
        #print(testpt)
        if peg.pt_inside(testpt.x,testpt.y):
            #print(testpt,numsteps)
            new_size = numsteps * vel_vector.get_size()
            col_vect = vel_vector.scalar_mult(new_size)
            
            return col_vect