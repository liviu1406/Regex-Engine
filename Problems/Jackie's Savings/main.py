def final_deposit_amount(*interest, amount=1000):
    for i in interest:
        amount += amount * (float(i) / 100)
    return round(amount, 2)


# print(final_deposit_amount(5, 3, 1))
