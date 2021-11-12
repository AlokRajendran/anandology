# Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def filter(f,a):
   return [x for x in a if f(x) is True]
def even(p):
   return p%2==0
l=[1,2,3,4]
print('Original list',l)
print(filter(even,l))