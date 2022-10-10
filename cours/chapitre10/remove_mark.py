s = "Nobody expects the Spanish Inquisition!# In fact, those who do expect the Spanish Inquisition..."
ch = s.find( "#" )
print(ch)
s = s[:ch] + s[ch+1:]
print( s )
