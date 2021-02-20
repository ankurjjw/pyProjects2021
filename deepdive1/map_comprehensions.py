l1 = [1, 2, 3, 4, 9, 10]
l2 = [5, 6, 7, 8]

l3 = list(map(lambda x, y: x + y, l1, l2))
print(l3)

print([x + y for x, y in zip(l1, l2)])

smaller_list = len(l1) > len(l2) and l2 or l1  # returns the smaller list
print([l1[i] + l2[i] for i in range(len(smaller_list))])
