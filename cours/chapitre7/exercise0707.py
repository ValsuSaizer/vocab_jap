from random import random
from math import sqrt

N_DARTS = 1000000
M = 0
pi = 0

for n in range( N_DARTS ):
    x = random()
    y = random()
    distance = sqrt( x*x + y*y )
    if distance <= 1:
        M += 1

pi = ( 4 * M ) / N_DARTS
print( "The approximation of pi is:", pi)
