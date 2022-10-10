from pcinput import getFloat

num1 = getFloat( "Please enter a first number: " )
num2 = getFloat( "Please enter a second number: " )
num3 = getFloat( "Please enter a third number: " )

maximum = "The maximum between {:.2f}, {:.2f} and {:.2f} is {:.2f}"
minimum = "The minimum between {:.2f}, {:.2f} and {:.2f} is {:.2f}"
average = "The average of {:.2f}, {:.2f} and {:.2f} is {:.2f}"
print( maximum.format( num1, num2, num3, max( num1, num2, num3 ) ) )
print( minimum.format( num1, num2, num3, min( num1, num2, num3 ) ) )
print( average.format( num1, num2, num3, ( num1 + num2 + num3) / 3  ) )
