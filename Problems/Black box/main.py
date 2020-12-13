# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]

var = blackbox(lst)

if id(var) == id(lst):
    print('modifies')
else:
    print('new')
