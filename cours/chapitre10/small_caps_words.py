s = "I'm sorry, sir."
output = ""
for ch in s:
    if ch >= "A" and ch <= "Z":
        output += ch.lower()
        continue
    elif ch >= "a" and ch <= "z":
        output += ch
        continue
    output += " "

output = output.split()
print( output )
