#Write a function such that consumes an int as its argument returns True only if the following conditions are met:

# Conditions are
# odd number of digits
# has a zero in the center ,but nowhere else


def check_num(num):
    """
    Returns True if the input integer has an odd number of digits and has a zero in the center,
    but nowhere else. Returns False otherwise.
    """
    num_str = str(num)
    ''' This line converts the integer `num` into a string `num_str`.
    We do this to check whether the number of digits in `num` is odd or even,
    and to use string operations to check if the zero is in the center
    and to check if there is any other zero in the rest of the digits
    '''
    if len(num_str) % 2 == 0:
        ''' This checks if the length of `num_str` is even,
        which means the number of digits in `num` is even.
        If this is the case, the function returns `False`,
        as we need an odd number of digits for the other conditions to be satisfied.
        '''
        return False
    
    zero_index = len(num_str) // 2
    ''' This line calculates the index of the center digit in `num_str`.
    Since the length of `num_str` is odd,
    we can get the index of the center digit by performing integer division by 2 (`//`),
    which gives us the floor division
    '''
    if num_str[zero_index] != '0':
        '''This checks if the center digit of `num_str` is `0`. If it's not `0`
        , the function returns `False`, 
        as the center digit must be `0` for the other conditions to be satisfied.
        '''
        return False
    
    if '0' in num_str[:zero_index] or '0' in num_str[zero_index+1:]:
        '''This checks if there is any other `0` digit in `num_str`,
        excluding the center digit. We use slicing to split `num_str` into two parts,
        before and after the center digit. If either of these parts contains a `0`,
        the function returns `False`
        '''
        return False
    
    return True
