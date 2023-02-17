a=[1,2,3]
b=[1,3]

def find_even(l):
    '''
Assumes l as a list
Raises a value error if no even no is present
'''
    for i in l:
        if i%2==0:# Even num found
            break

    else:
        raise ValueError('No even no found')
