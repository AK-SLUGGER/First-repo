

##15-02-2023


##Rise an error

a=[1,2,3]
b=[7,8,0]

for i in range(len(a)):
    try:
        print(a[i]/b[i])
    except ZeroDivisionError:
        raise ZeroDivisionError('Please make sure all the elements of list are non zero')
    
