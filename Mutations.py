"""python program to change or add a char in the string"""

def mutate_string(string,pos,character):
    l=list(string)
    l[pos]=character
    string="".join(l)
    return string

string="HARISHISJOKER"
mutable_string=mutate_string(string,3,'k')
print(mutable_string)