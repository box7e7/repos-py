def compare(str,name): 

	var=[]
	var1=[]
	k=0
	f=0
	var4=[]
        

	for i in str:
		var.append(i.lower())
	for j in name:
		var1.append(j.lower())

	k=len(var)
	f=len(var1)
	
	sss=0
	for j in range(0,f):

		for i in range(sss,k):
			if var[i]==var1[j]:
				
				sss=i+1
				var4.append(i)
	 			
				break


	if len(var4)==f:	
		return True
	else:
		return False

	
