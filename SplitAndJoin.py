"""python program to split and join """

def split_join(line):

    a=line.split(" ")
    b="*".join(a)
    return b

line="python is easy to learn"
result=split_join(line)
print(result)