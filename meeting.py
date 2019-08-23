def meeting(s):
    dict1={}
    str1=""
    for element in s.split(';'):
        
        x=element.split(':')
        print(x)
        dict1.update({x[0].upper():x[1].upper()})
    
    dict2={}
    print(dict1)
    sorted_last=sorted(dict1.values())
    sorted_first=sorted(dict1.keys())
    for i in sorted_last:

        for j in sorted_first:
            
            if dict1[j]==i:
                dict2.update({j:i})
                sorted_first.remove(j)
                break
                
    for i in dict2:
        str1+=f'({dict2[i]}, {i})'
    #print(dict1)    
    #print(dict2)  
    return str1
