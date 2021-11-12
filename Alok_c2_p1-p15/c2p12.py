# Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
#  group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

def group(l,size):
    length = len(l)
    new = []
    for i in range(0,length):
        for j in range(i,size):
            new[i].append(l[j])
    print(new)

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))