result = 1
num1 = 0
num2 = 0
while result < 1000:
    if num1 == 0 and num2 == 0:
        num2 += 1
    print( result )
    result = num1 + num2
    num1 = num2
    num2 = result

print( "Done.")
