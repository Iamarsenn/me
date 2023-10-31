def meeeh(array1):
    if len(array1) >= 2:
        del array1[0]
        del array1[-1]
    else:
        print()
        pass

def middle(array1):
    if len(array1) >= 2:
        return array1[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4, 5]
meeeh(my_list)
print("changed list",my_list)

my_list = [1, 2, 3, 4, 5]
result = middle(my_list)
print("new list",result)
