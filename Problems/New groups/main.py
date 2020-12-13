# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
dictionary = {group: None for group in groups}
num_groups = int(input())

for i in range(0, num_groups):
    dictionary[groups[i]] = int(input())

print(dictionary)
