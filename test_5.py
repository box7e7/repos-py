def indexes(arr, num):
	index=[]
	for i, x in enumerate(arr):
		if x == num:
            		index.append(i)
	return index


def remove_duplicate_words(s):

	var=[]
	var=s.split()
	for i in var:
		print(i)
	return var
