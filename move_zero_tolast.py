"""python program to move the zero from the list to last place"""

list=[1,7,9,0,4,3,2]
for item in list:
    if item==0:
        list.remove(item)
        list.append(item)
print(list)