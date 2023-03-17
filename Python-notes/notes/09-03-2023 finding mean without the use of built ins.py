


### to find the mean without using built ins

## sum_list

## length_list

## mean_list

'''
r=[1,2,56,90]
sum_r=sum_list(r)
length_r=length_list(r)
mean_r=mean_list(r)
'''


# sum_list
def sum_list(list_name):
    '''Argument is a list of ints
       Returns an int
       '''
    sum_list=0 # Accumulates the sum of elements in the list
    for i in r:
       sum_list=sum_list+i
            
    return sum_list
    
    

#length_list

def length_list(list_name):
    '''Argument is a list
       Returns an int which is the total no of elements in the list
    '''
    count=0# Counts the num of elements in the list
    for i in r:
       count=count+1
        
    return count
    
    

# mean_list
def mean_list(list_name):
    '''Arguments is a list
       Returns a float which is the mean of the list
          '''
    mean_list=sum_list(list_name)/length_list(list_name)

    return mean_list



r=[1,2,56,90]

sum_r=sum_list(r)
length_r=length_list(r)
mean_r=mean_list(r)

print('Mean=',mean_r)
