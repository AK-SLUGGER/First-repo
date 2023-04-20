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
    if len(num_str) % 2 == 0:
        return False
    
    zero_index = len(num_str) // 2
    
    if num_str[zero_index] != '0':
        return False
    
    if '0' in num_str[:zero_index] or '0' in num_str[zero_index+1:]:
        return False
    
    return True
