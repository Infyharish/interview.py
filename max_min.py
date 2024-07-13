"""program to find maximum and minimum value in an array"""

arr=[12,34,22,123,43]
max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)


arr=[12,34,22,123,43]
min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)