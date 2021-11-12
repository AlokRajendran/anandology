# Problem 10: Write a function unique to find all the unique elements of a list.
# unique([1, 2, 1, 3, 2, 5])

a = [1, 2, 1, 3, 2, 5]

def unique(a):
    u = []
    for i in a:
        if i not in u:
            u.append(i)
    
    return(u)

print(unique(a))

