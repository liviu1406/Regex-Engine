def list_sum(some_list):
    if some_list == []:
        return 0
    elif some_list == 0:  # base case
        return some_list[0]
    else:
        return some_list[0] + list_sum(some_list[1:])   # recursive case


# print(list_sum([5]))
