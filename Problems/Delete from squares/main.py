# squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

del_key = int(input())

return_value = squares.pop(del_key, "There is no such key")
print(return_value)
print(squares)
