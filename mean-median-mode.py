# mean - the average value of all the values
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1) / len(list1)
print(mean)

# median - the middle value among all the values in sorted order
list1.sort()
if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)

# mode - the most frequently occuring value among all the values
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)
