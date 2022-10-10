allthings = {"Socrates", "Plato", "Erathosthenes", "Zeus", "Hera", "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Erathosthenes"}
mortalthings = { "Socrates", "Plato", "Erathosthenes", "Cat", "Dog" }

# a) all men are mortals
print( "All men are mortals because in mortals, we find {}, all men are {} and all mortal mens are{}".format( mortalthings, men, men.intersection( mortalthings ) ) )
# b) Socrates is a man
for element in men:
    if element == "Socrates":
        print( "Socrates is a man" )
# c) Socrates is mortal
for element in mortalthings:
    if element == "Socrates":
        print( "Socrates is mortal" )
# d) there are mortal things that are not men
print( "There are mortal things that are not men :", mortalthings - men )
# e) there are things that are not mortal
print( "There are things that are not mortal :", allthings - mortalthings )
