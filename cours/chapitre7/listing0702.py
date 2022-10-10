from pcinput import getInteger

total = 0
count = 0
repetition = int( input( "How many repetition do you want ? (integer please) " ) )
while count < repetition:
    total += getInteger( "Please give a number: " )
    count += 1

print( "Total is ", total )
print( "Average is" , total / repetition )
