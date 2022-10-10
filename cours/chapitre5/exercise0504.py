from math import exp

exponential = "The values of exponential are :\nPower -1: {:^10.5f}\nPower 0: {:^10.5f}\nPower 1: {:^10.5f}\nPower 2: {:^10.5f}\nPower 3: {:^10.5f}"
print( exponential.format( exp(-1), exp(0), exp(1), exp(2), exp(3) ) )
