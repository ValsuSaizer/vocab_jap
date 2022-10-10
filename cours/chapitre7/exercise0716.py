from random import randint

CRAWLERS = 100000
cumulated_days = 0

for x in range( CRAWLERS ):
    days = 0
    previous = 0
    choice = 1
    if days == 0:
        choice = randint( 1, 3 )
        if choice == 3:
            continue
        else:
            days += 1
    while True:
        choice = randint( 1, 2 )
        if choice == 1:
            days += 1
            continue
        else:
            cumulated_days += days
            break
    
print( "The average age that a Triangle Crawler reaches is {:.2f} days.".format ( cumulated_days / CRAWLERS ) )
