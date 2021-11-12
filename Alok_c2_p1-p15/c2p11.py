# Problem 11: Write a function dups to find all duplicates in the list.
# dups([1, 2, 1, 3, 2, 5])

a = [1, 2, 1, 3, 2, 5]

def dups(a):

    l = []
    dup = []
    for i in a:
        if i not in l:
            l.append(i)
        else:
            dup.append(i)

    return dup

print(dups(a))