#program to swap first and third element in the list.

mylist=[12,23,34,45]
pos1,pos2=0,2

fir_ele=mylist.pop(pos1)
sec_ele=mylist.pop(pos2-1)

mylist.insert(pos1,sec_ele)
mylist.insert(pos2,fir_ele)
print(mylist)