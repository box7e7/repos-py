while True:
    answer=input("Do you want to compute the Total y/n: ")
    if answer.lower()=="y":
        sub_total=input("Enter sub_total: ")
        
        while True:
            try:
                val=float(sub_total)
                
                break
            except ValueError:
                    sub_total=input("Please reenter sub_total: ")
                    
        tip = input('Enter the tip as percentage: ')
        tip = float(tip)
        total = val * 1.0825 + (tip/100) * val
        print(total)
    elif answer.lower() == 'n':
        print('Good bye')
        break
    else:
        continue
