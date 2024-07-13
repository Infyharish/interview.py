def cap_string(s):
    return s.title()

s=" welcome to python"
result=cap_string(s)
print(result)


def capitalize(s):
    ans=s.split(' ')
    ans1=((i.capitalize() for i in ans))
    return ' '.join(ans1)


s="welcome to python programming"
result=capitalize(s)
print(result)