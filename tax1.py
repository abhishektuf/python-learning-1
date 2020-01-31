paid_amount = float(input('Price you paid...: '))
state = input('Indian state please: ')


def state_tax(province, price):
    if province.lower() == 'haryana':
        tax = 0.45 * int(price)
    elif province.lower() == 'delhi':
        tax = 0.55 * int(price)
    elif province.lower() == 'rajasthan':
        tax = 0.76 * int(price)
    else:
        tax = 0.18 * int(price)
    return tax


calculated_tax = float(state_tax(state, paid_amount))

total_price = paid_amount + calculated_tax

print('Total price you pay (including all taxes): ' + str(total_price))

'''
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


'''
