


'''Finding an even no by try & except'''

def find_even_2(l):

    i=0
    try:
        while l[i]%2==0:
            i+=1# Continue check next element in the list if l[i] is odd
    except IndexError:
        raise ValueError('No even no found')
    else:
        return l[i]
