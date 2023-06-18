#price of a house i s $1M
#if buyer has good credit, they need to put down 10%
#otherwise the need to put down 20%

price = 1000000
has_good_credit = False
if has_good_credit:
    down_payement = 0.1 * price
else:
    down_payement = 0.2 * price
print(f"down payement is ${down_payement}")
