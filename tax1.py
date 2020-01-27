price = 10

# calculating the tax on food items inside Canada.
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

given_price = input('amount you paid?: ')

given_price = float(given_price)
if given_price >= 1.00:
    tax = 0.07
    print('Tax rate is : '+str(tax))
else:
    tax = 0.00
    print('Tax rate is free :'+str(tax))