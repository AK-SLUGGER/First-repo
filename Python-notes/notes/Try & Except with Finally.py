

### Try & Except with finally

try:
    result=12/0
except ZeroDivisionError:
    print('Please use a non-zero num as adivisor')
else:
    # if there is no exception this block is executed
    print('Block 3')
finally:
    #This block is executed irrespective of previous blocks
    print('Always Executed')
    
print('2nd line')
