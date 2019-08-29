def next_version(version):
    result=""
    dots=0
    str1=version
    list1=str1.split('.')
    num1=''.join(list1)
    num1=str(int(num1)+1)
    
    for i in str1:
        if i==".":
            dots+=1
    
    for i in range(1,dots+1):
        result=f'.{num1[-i]}'+result
    result=f'{num1[0:len(num1)-dots]}'+result  
    if result[0]==".":
        result=f'0{result[0:len(result)]}'
    return result   
