def capitalize(s):
    result=[]
    str2=""
    str3=""
    for i in range(0,len(s)):
        if i%2==0:
            str2+=s[i].upper()
            str3+=s[i]
        else:
            str2+=s[i]
            str3+=s[i].upper()
    result.append(str2)
    result.append(str3)
    return result
