cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
s = 0


for a in range(6):
    i = input()
    for k, v in cards.items():
        if i in k:
            s += v
avg = s / 6
# print(s)
print(avg)






