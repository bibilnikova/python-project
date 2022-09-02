def merge2Lists(i, j):
    mergedlist = []
    while (i and j):
        if (i[0] <= j[0]):
            item = i.pop(0)
            mergedlist.append(item)
        else:
            item = j.pop(0)
            mergedlist.append(item)
    mergedlist.extend(i if i else j)
    return mergedlist


list1 = [1, 2, 3, 5, 7, 8]
list2 = [4, 6, 9, 9, 0]
print(merge2Lists(list1, list2))

