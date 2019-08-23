def number_of_pairs(gloves):
    
    count=0
    list1=[]
    for i in gloves:
        if i not in list1:
            list1.append(i)
            count+=gloves.count(i)/?2
    return  count 
