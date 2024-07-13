nterms=int(input("how many terms : "))
n1=0
n2=1
print(n1)
print(n2)
for i in range(0,nterms+1) :
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum