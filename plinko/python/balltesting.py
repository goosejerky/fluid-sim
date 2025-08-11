import pegs
from balls import *

testball = Ball(0,0)
testvel = Vector(1,2)

print(testball.history)

testball.update_position(testvel)

print(testball.history)