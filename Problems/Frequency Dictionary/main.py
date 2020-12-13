# put your python code here
user = input().lower().split()

myList = [x for x in user]

a_dict = dict((i, myList.count(i)) for i in myList)

for k, i in a_dict.items():
    print(k, i)

