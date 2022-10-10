from pcinput import getInteger

count = 1
iteration = getInteger( "How many iteration do you want ? (Please enter an integer for this) " )
question = "Number {:d}:"
summup = 0
while count < iteration:
    number = getInteger( question.format ( count ) )
    count += 1
    summup += number
print( "Total is", summup )
