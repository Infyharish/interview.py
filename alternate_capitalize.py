"""
Write a function that takes in an argument sentence which capitalizes every alternate character it"""

def word(sentence):
    st=[]
    
    for i in range(len(sentence)):
        if i%2!=0:
            st.append(sentence[i].upper())
        else:
            st.append(sentence[i].lower())
        

sentence='welcomeopythonprogramming'
result=word(sentence)
print(result)
# str="balaji"
# str(15)
# str()
# word()
# akshaya(a,b,c)
# str(len(sentence))

def my_func(st):

    res = []
    #Iterate over the character
    for index in range(len(st)):
        if index % 2 == 0:
            #Refer to each character via index and append modified character to list
            res.append(st[index].upper())
        else:
            res.append(st[index].lower())

    #Join the list into a string and return
    return ''.join(res)

word="Welcome to python"
result=my_func(word)
print(result)