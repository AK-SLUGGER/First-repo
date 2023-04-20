# even no

a=[1,2,3]
b=[1,3]

def find_even(L):
    '''Assumes L as a list
       Raise a Value error if no even number is present
       '''
    for i in a:
        
        if i%2==0:#Even no found
            
            break
        else:

            raise ValueError('No even no found')
        


