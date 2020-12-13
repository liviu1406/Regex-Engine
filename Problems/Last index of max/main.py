def last_indexof_max(numbers):
    # write the modified algorithm here
    index = 0

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[index]:
            index = i

    return index


all_numbers = list(map(int, input().split()))

print(last_indexof_max(all_numbers))
