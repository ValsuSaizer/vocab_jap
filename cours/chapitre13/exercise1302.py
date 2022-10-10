movies = ["Monty Python and the Holy Grail",
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

grail_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5, 8 ]
brian_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]
life_ratings = [ 7, 6, 5 ]
different_ratings = [ 6, 5, 6, 6 ]

moviedict = {}

for entry in movies:
    if entry == "Monty Python and the Holy Grail":
        moviedict[ entry ] = grail_ratings
    elif entry == "Monty Python's Life of Brian":
        moviedict[ entry ] = brian_ratings
    elif entry == "Monty Python's Meaning of Life":
        moviedict[ entry ] = life_ratings
    elif entry == "And Now For Something Completely Different":
        moviedict[ entry ] = different_ratings

ratesum = 0
for film in moviedict:
    for note in moviedict[film]:
        ratesum += note
    print( film, round( ratesum/len( moviedict[film] ) ) )
    ratesum = 0
