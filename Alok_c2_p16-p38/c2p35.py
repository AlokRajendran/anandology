# Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

import sys
def freq(x):
 dict = {}
 for i in x:
  dict[i] = dict.get(i,0) + 1
 return dict

a=input("enter a string")
print(freq(a))