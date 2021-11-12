# Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a 
# function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?


a= [1, 2, 3, 4]

def cumulative_sum(a):
    b = 0
    c = []
    for i in a:
        b += i
        c.append(b)
    return c

print (cumulative_sum(a))