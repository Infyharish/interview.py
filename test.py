"""python program to write a function that takes in an argument sentence which reverses only the words in it"""
def word(sentence):
    a=sentence.split()
    for i in a:
        b=i[::-1]
        print(b,end=" ")
        
sentence="welcome to python"

word(sentence)


elems=['A','B','C','D']
nums=['1','2','3','4']
result=zip(elems,nums)
print(list(result))