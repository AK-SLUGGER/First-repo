


def print_odds(odd_num):
    '''Assumes odd_num as an int
       Prints first odd_num integers
       Returns None
    '''
    Limit=2*odd_num
    n=0
    while(n<=Limit):
        if(n%2!=0):
            print('Odd no:',n)
        n=n+1


o=int(input('Please enter the number'))
print_odds(o)
                   
