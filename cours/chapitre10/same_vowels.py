expr1 = "The Holy Grail"
expr2 = "Life of Brian"
progress = ""
i = 0

while i < len( expr1 ):
    progress += expr1[i]
    if expr1[i] in expr2 and expr1[i] == expr2[i]:
        print( expr1[i] )
        print( len(progress) - 1 )
    i += 1
