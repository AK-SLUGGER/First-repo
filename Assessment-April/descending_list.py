
# April- Assessment
# Write a code that checks whether the items in a descending order


def descending(seq):

    '''param:


        seq:list

        returns:

        bool


        Cosumers list and return True if list is in descending order else returns false

        '''
    status = sorted(seq,reverse = True) == seq
    return status
    
