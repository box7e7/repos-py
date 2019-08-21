def duplicate_count(text):
    list2=[ ]
    list1=[]
    Result=[]
    str=text
    
    for i in range(0,len(str)):
        list1.append(str[i].lower())
               

    for i in list1:
        if i not in Result:
            Result.append(i)
        
    print(Result)  

    for i in range(0,len(Result)):
    
        k=0
        for j in list1:
            if Result[i]==j:
                k+=1
        list2.append(k)        
            
      
    count=0
    for i in list2:
        if i>1:
            count+=1
    return count       
        
     
