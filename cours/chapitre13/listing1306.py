text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

splitedtext = text.split( "," )

courses = {}
for x in splitedtext:
    if x not in courses.keys():
        courses[ x ] = 1
    else:
        courses[ x ] += 1

print( courses )
