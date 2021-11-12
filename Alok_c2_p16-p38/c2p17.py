# Problem 17: Write a program to print lines of a file in reverse order.


# file = open("she.txt","r")
# a = file.readlines()
# t = reversed(a)
# for i in t:
#     print(i.rstrip())      
      

f=input("Enter file name: ")
a = reversed(list(open(f).read()))
for i in a:
    print(i.rstrip())