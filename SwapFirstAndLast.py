# program to swap first and last element of an array

mylist=[12,23,43,43,77]
size=len(mylist)
t=mylist[0]
mylist[0]=mylist[-1]
mylist[-1]=t
print(mylist)

# approach 2 
mylist=[12,23,43,54,77]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print(mylist)

# approach 3 using * operand

mylist=[12,23,43,54,77]
start,*middle,end=mylist
mylist=[end,*middle,start]
print(mylist)