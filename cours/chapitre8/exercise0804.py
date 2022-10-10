from pcinput import getInteger
from math import sqrt

# The function quadraticFormula gives the possible solutions of the equation Ax² + Bx + C = 0
# The function takes 3 integer as parameters
# Depending on parameters value, different conditionals are applied

num1 = getInteger( "Please enter a value for first factor: " )
num2 = getInteger( "Please enter a value for second factor: " )
num3 = getInteger( "Please enter a value for third factor: " )

def quadraticFormula( a, b, c ):
    if a == 0 and b == 0:
        return "There's only one solution as A and B are equal to 0, there's only C remaining which equals to {}.".format( c )
    elif a == 0:
        return "There's only one solution because a = 0, it remains -C / B ==> {}.".format( -c / b )
    elif b*b - ( 4 * a * c ) < 0:
        return "There's no solution to this equation as B² - 4AC = {}.".format( b * b - 4 * a * c )
    elif b*b - ( 4 * a * c ) == 0:
        return "There's only one solution because the value under the square root is equal to 0, it remains -B / 2A ==> {}i.".format( -b / ( 2 * a ) )
    else:
        return "There are two solutions, first is (-B + sqrt(B² - 4AC))/2A ==> {} and the second one is (-B - sqrt(B² - 4AC))/2A ==> {}.".format( (-b + sqrt( b*b - 4 * a * c ) ) / 2 * a, (-b -sqrt( b * b - 4 * a * c ) ) / 2 * a )

print( quadraticFormula( num1, num2, num3 ) )
