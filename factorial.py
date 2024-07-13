num=int(input("enter a number:"))
fact=1
if num<0:
    print("enter a positive number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of",num, "is",fact)


"""using recursion function"""

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("enter a num"))
print(fact(n))

