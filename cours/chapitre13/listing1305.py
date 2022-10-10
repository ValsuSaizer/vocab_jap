wordlist = ["apple","durian","banana","durian","apple","cherry","cherry","mango","apple","apple","cherry","durian","banana","apple","apple","apple","apple","banana","apple"]
value = 0
courses = {}
for x in wordlist:
    if x not in courses.keys():
        courses[ x ] = 1
    else:
        courses[ x ] += 1

print( courses )
