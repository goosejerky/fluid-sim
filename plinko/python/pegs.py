class Peg:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
        
    def pt_inside(self,x,y):
        
        xdiff = (self.center_x - x)**2
        ydiff = (self.center_y - y)**2
        dist = (xdiff + ydiff)**0.5
        
        return (dist <= self.radius)