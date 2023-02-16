n= input('Enter a number')# User input

count =0# Put & store sum of digits here
for i in n:
    if i.isdigit():
        count+=int(i)

print(count)        


## use of func

n= input('Enter a number')# User input


def sumDigits(s):
    
    '''Assumes s as str
Returns sum of digits'''
    
    count =0# Put & store sum of digits here
    for i in n:
        
        if i.isdigit():
            count+=int(i)
            return count

print(sumDigits(n))      
