from pcinput import getInteger

divisible_by_3 = 0
smallest = 0
largest = 0

for indicator in range( 10 ):
    number = getInteger( "Please enter the number {}: ".format( indicator + 1 ) )
    if indicator == 0:
        smallest = number
        largest = number
    if number % 3 == 0:
        divisible_by_3 += 1
    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number
print( "From the 10 entered numbers, the largest is {}, the smallest is {} and there was {} cases of numbers divisible by 3.".format( largest, smallest, divisible_by_3 ) )
