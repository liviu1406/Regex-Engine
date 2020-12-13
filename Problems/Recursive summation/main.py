def rec_sum(n):
    if n < 0:
        print('no solution')
    elif n == 0:
        return 0
    else:
        return n + rec_sum(n-1)


# print(rec_sum(3))
