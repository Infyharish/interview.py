""""program to convert lower to upper string and upper to lower string"""

def swap_case(s):
    s=""
    for i in s:
        if i.islower==True:
            s+=i.upper()
        elif i.isupper==True:
            s+=i.lower()
        else:
            s+=i
    return s

s="HariSH"
result=swap_case(s)
print(result)


def swap(s):
    return s.swapcase()

input_string="HaRiSh"
swapped_string=swap(s)
result=print(swapped_string)