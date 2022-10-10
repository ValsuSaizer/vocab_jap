set1 = { "A", "B", "C" } 
set2 = { "B", "C", "D" }

unionset = ( set1 | set2 ) - (set1 & set2)

print( unionset )
