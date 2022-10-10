s = "blablibloup"
mask = (1<<5) | (1<<3) | (1<<1)
encoded = ""

print( s )

for c in s:
    encoded += chr( ord(c) ^ mask )
print( encoded )

s = ""
for c in encoded:
    s += chr( ord(c) ^ mask )
print( s )
