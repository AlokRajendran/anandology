# Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.
# cumulative_product([1, 2, 3, 4])



a = [1,2,3,4]

def cumulative_product(a):
    b = 1
    c = []
    for i in a:
        b *= i
        c.append(b)
    return b

print(cumulative_product(a))