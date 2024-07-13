mylist=[12,12,23,12,34,54]
x=12
count=0
for i in mylist:
    if(i==12):
        count=count+1
print(count)

# approach 2 using count()

mylist=[10,20,10,30,10,35]
x=int(input("enter the number to be counted: "))
y=mylist.count(x)
print(y)


# approach 3 using counter()
from collections import Counter
mylist=[10,20,10,30,10,35]
x=10
dic=Counter(mylist)
print(f'{x} has occured {dic[x]} times')