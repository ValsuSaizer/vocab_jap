DOLLARS_AS_CENT = 100
QUARTERS_AS_CENT = 25
DIMES_AS_CENT = 10
NICKELS_AS_CENT = 5
PENNIES_AS_CENT = 1
"""First, the amount of money to be analyzed"""
amount_of_money = 1389
"""Second, how many dollars fits in the amount of money"""
dollars = amount_of_money // DOLLARS_AS_CENT
amount_of_money -= dollars * DOLLARS_AS_CENT
print( "After counting dollars, it remains : ", amount_of_money )
"""Third, how many quarters fits in the remain amount of money"""
quarters = amount_of_money // QUARTERS_AS_CENT
amount_of_money -= quarters * QUARTERS_AS_CENT
print( "After counting quarters, it remains : ", amount_of_money )
"""Fourth, how many dimes fits in the remain amount of money"""
dimes = amount_of_money // DIMES_AS_CENT
amount_of_money -= dimes * DIMES_AS_CENT
"""Fifth, how many nickels fits in the remain amount of money"""
print( "After counting dimes, it remains : ", amount_of_money )
nickels = amount_of_money // NICKELS_AS_CENT
amount_of_money -= nickels * NICKELS_AS_CENT
print( "After counting quarters, it remains : ", amount_of_money )
"""Sixth, how many pennies fits in the remain amount of money"""
pennies = amount_of_money // PENNIES_AS_CENT
amount_of_money -= pennies * PENNIES_AS_CENT
print( "After counting quarters, it remains : ", amount_of_money )
"""Seventh, Here's the amount of coins you need in total"""
print( amount_of_money )
amount_of_money = dollars * DOLLARS_AS_CENT + quarters * QUARTERS_AS_CENT + dimes * DIMES_AS_CENT + nickels * NICKELS_AS_CENT + pennies * PENNIES_AS_CENT
print( "Money set:", amount_of_money )
print( "Dollars:", dollars )
print( "Quarters:", quarters )
print( "Dimes:", dimes )
print( "Nickels:", nickels )
print( "Pennies:", pennies )
print( "The minimum number of coins needed to get ", amount_of_money, " is ", dollars + quarters + dimes + nickels + pennies )
