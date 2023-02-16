

#Sum of digits by try & Except

def sumDigits2(s):
    
    '''Assumes s as str
Returns sum of digits'''
    
    count =0# Put & store sum of digits here
    for i in s:
        try:
            count+=int(i)
        except ValueError:
            continue
        return count

            
        
n= input('enter a no \n')# User input


print(sumDigits2(n))
        
