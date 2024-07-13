from string import digits,ascii_lowercase
def missingCharacters(s):
    
    r="".join(c for c in digits+ascii_lowercase if c not in s)
    return r


s="abcd1235"
r=missingCharacters(s)
print(r)