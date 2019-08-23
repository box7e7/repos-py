def number_of_pairs(gloves):
    k=0
    count=0
    list1=[]
    for i in gloves:
        if i not in list1:
            list1.append(i)
    for i in list1:
        k=0
        for j in gloves:
            if i==j:
                k=k+1
        count+=int(k/2)        
                
            
    return  count 
