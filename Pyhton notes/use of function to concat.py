'''
use of function
'''
def concate_n_times(string_concat,num_concat):#function signature
    concatenated_string=string_concat*int(num_concat)#function body
    concatenated_string=concatenated_string.upper()
    print(f'inside concate_n_times.concatenates_string{concatenated_string}')
    return concatenated_string

string_1='abhishek'
n_concat=input('how many times shall i concatenate\n')
new_string=concate_n_times(string_1,n_concat)
new_string_2=concate_n_times(string_1,int(n_concat)-1)#concatenate 1 less time than upper
print(f'new_string={new_string}')
print(f'new_string_2={new_string_2}') 

