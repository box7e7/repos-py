def fizzbuzz_plusplus(list1, list2):
  # TODO: complete
  
  
  


    result=[]
    var=1
    for i in list1:
        var=var*i

    str1=""
    for i in range(1,var+1):
        str1=""
        for n1,n2 in zip(list1,list2):
            if i%n1==0:
                str1+=n2

        result.append(str1)

        for i in range(0,len(result)):
            if result[i]=='':
                result[i]=i+1

    return result

