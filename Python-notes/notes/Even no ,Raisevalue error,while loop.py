







# Raise a valueError if No even no. is present
#num%2==0 if this is True then num is even
l=[1,2,5]
def find_even_2(l):
    '''Assumes l as a list of numbers to
       Returns the first even  no in the list
       Raises ValueError if no even no is present
       '''
    
    i=0
    try:
        while (l[i]%2)!=0:#Keep on checking untill[i] is odd
            
            #print(f'i={i},l[i]={l[i]}')
            #print(f'l[i]%2,{l[i]%2}')
            #print(f'while loop condition-> (l[i]%2)!=0:{(l[i]%2)!=0}')
            

            i+=1
            
    except IndexError:
        #Indexerror occour when allthe even in list are odd
         raise ValueError('No even no found')
    return l[i]
    
        
    
    
      
