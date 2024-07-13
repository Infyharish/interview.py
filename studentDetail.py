from collections import OrderedDict
a=OrderedDict()

for i in range(int(input())):
    student,space,marks=input().rpartition(' ')
    if student not in a:
        a[student]=int(marks)
    else:
        a[student]+=int(marks)
for i in a.items():
    print(i)