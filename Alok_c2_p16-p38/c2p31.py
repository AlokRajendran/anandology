# Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

import sys

def parse_csv(filename,d,c):
   return [x[:-1].split(d) for x in open(filename,'r').readlines() if x[0]!=c]
filename=sys.argv[1]

delim= input("Enter the delimiter:")
comment= input("Enter the comment indicator:")
print('parse_csv(',filename,',',delim,',',comment,')=',parse_csv(filename,delim,comment))