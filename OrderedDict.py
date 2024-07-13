""" You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence."""

from collections import OrderedDict
a=OrderedDict()
for i in range(int(input())):
    itemName,space,price=input().rpartition(':')
    if itemName not in a:
        a[itemName]=int(price)
    else:
        a[itemName]+=int(price)
for i in a.items():
    print(i)