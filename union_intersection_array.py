def union(list1, list2):
    new_arr = []
    for i in list1:
        if i not in new_arr:
            new_arr.append(i)
    for i in list2:
        if i not in new_arr:
            new_arr.append(i)
    new_arr.sort()
    print("Union of above two array: ", new_arr)


def intersection(list1, list2):
    new_arr = []
    for i in list1:
        if (i in list1) and (i in list2):
            new_arr.append(i)
    new_arr.sort()
    print("Intersection of above two array: ", new_arr)


# Declare two empty list list1 and list2
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

# original lists
print("list 1=", list1)
print("list 2=", list2)

# call the function union
union(list1, list2)

# call the function intersection
intersection(list1, list2)
