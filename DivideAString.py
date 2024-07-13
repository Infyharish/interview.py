"""using textwrap function to divide a string"""
import textwrap
def wrap(string,max_width):
    return textwrap.fill(string,max_width)

string=input("enter a string : ")
width=int(input("enter the width : "))

result=wrap(string,width)
print(result)


"""program to divide the string in sorted order using itertools.combination()"""
from itertools import combinations
s,k=input().split()
k=int(k)
for i in range(1,k+1):
    for j in combinations(list(sorted(s)),i):
        print(''.join(j))


# this program divides the string into equal parts based on the width entered .