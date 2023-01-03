'''   '''
#def means define(user defined function)
def concate_n_times(string_concat,num_concat):
    concatenated_string = string_concat*int(num_concat)
    return concatenated_string

string_1='abcd'
n_concat = input('how many times shall i concatenate\n')
new_string = concate_n_times(string_1,n_concat)
print(new_string)

