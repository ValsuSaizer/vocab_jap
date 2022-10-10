prime_num = []
limit = 187

for i in range( 1, limit+1 ):
    prime_num.append( i )
prime_num.pop( 0 )
print ( prime_num )

for j in prime_num:
    if j == 0:
        prime.num.remove( j )
    for x in prime_num:
        if x%j == 0 and x != j:
            prime_num.remove(x)

print( prime_num )
