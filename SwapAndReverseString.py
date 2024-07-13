def reverse_words_order_and_swap_cases(sentence):
    
    b=sentence.split()
    c=b[::-1]
    d=' '.join(c)
    a=d.swapcase()
    return a

sentence=" hARISH is DeludED fOOL"
result=reverse_words_order_and_swap_cases(sentence)
print(result)