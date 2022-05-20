def capitalize_first_last_letter(str1):
    str1=res=str1.title()
    res=""
    for word in str1.split():
        res+=word[:-1] + word[-1].upper() + " "
    return res[:-1] 
print(capitalize_first_last_letter('python is a high level programming language'))
