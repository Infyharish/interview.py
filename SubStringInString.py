# """python program to count the number of substrings in string"""

# def count_sub(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         if string[i:len(string)].startswith(sub_string):
#             count+=1
#     return count

# string="the the gofjd sk"
# substring="the"
# result=count_sub(string,substring)
# print(result)


# def substring(string,sub):
    
#     if sub in string:
#         print("yes")
#     else:
#         print("no")
# string="messi is the greatest player of all time"
# sub="messi12"
# substring(string,sub)


def count_str(string,substring):
    count=string.count(substring)
    return count
string="harish harish messi ronaldo"
substring="harish"
print(count_str(string,substring))
