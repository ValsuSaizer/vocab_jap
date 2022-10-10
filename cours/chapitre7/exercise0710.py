from pcinput import getInteger

num = getInteger( "Please enter an integer: " )
divider = 2

if num == 1:
    print( "1 is forcibly a prime number... Please try again..." )
    exit()

while num%divider != 0:
    divider += 1

if divider == num:
    print( "Your number is a prime one!" )
else:
    print( "Your number is divisible by:", divider )
