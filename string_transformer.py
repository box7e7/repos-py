def string_transformer(s):

    s=s.swapcase()
    list1=s.split(' ')
    return ' '.join(list1[::-1])
       
