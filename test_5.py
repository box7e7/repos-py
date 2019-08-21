def indexes(arr, num):
	index=[]
	for i, x in enumerate(arr):
		if x == num:
            		index.append(i)
	return index


def remove_duplicate_words(s):

	var=[]
	var=s.split()
	result=[]
	
	for i in range(0,len(var)):
		if var[i]!="null":

			ins=indexes(var,var[i])
			for j in range(1,len(ins)):
				var[ins[j]]="null"
	
	for i in var:
		if i!="null":
			result.append(i)
	return result
