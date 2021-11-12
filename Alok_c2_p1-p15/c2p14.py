# Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and 
# use the return value of the key function to check for uniqueness.

# unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())

a = ["python", "java", "Python", "Java"]

def unique(a,key):
    u = []
    for i in a:
        if key(i) not in u:
            u.append(key(i))
    return u 

print(unique(a, key=lambda s: s.lower()))

