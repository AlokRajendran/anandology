# Problem 16: Write a function extsort to sort a list of files based on extension.



import os 


# def extsort(a): 
#     for i in range(0,len(a)): 
#         a[i]=a[i].split('.') 
#         a.sort(key=lambda a:a[1]) 
#     for i in range(0,len(a)): 
#         a[i]=".".join(a[i]) 
#         i=i+1 
#     return a 

# print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))

def extsort(a):
    i=0
    while(i<len(a)):
         a[i]=a[i].split('.')
         i=i+1
    a.sort(key=lambda a:a[1])
    i=0
    while(i<len(a)):
         a[i]=".".join(a[i])
         i=i+1 
    return a

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))