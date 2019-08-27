def score(dice):

    result=0
    li1=dice
    li3=[0,0,0,0,0,0]
  
    for i in range(1,7):
        if i==1:  ###one
            k=0
            count=0

            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*1000+count%3*100
        elif i==2: ###two
            k=0
            count=0
            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*200
        elif i==3: ##three
            k=0
            count=0
            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*300
        elif i==4: ##four
            k=0
            count=0
            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*400
        elif i==5: ##five
            k=0
            count=0
            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*500+count%3*50
        else:  ##six
            k=0
            count=0
            try:
                while k<len(li1)-1:
                    index1=li1.index(i,k,len(li1))
                    k=index1+1
                    count+=1
            except  ValueError:
                pass
            result+=count//3*600
    
    return result
