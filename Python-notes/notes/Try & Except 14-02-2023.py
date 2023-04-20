# Try & Except use


try:
    result=12/0
except ZeroDivisionError:
    print('Please use a non-zero num as adivisor')
print('2nd line')




#### with us eof else


try:
    result=12/0
except ZeroDivisionError:
    print('Please use a non-zero num as adivisor')
else:
    # if there is no exception this block is executed
    print('Block 3')
print('2nd line')
# Else block is not executed


try:
    result=12/2
except ZeroDivisionError:
    print('Please use a non-zero num as adivisor')
else:
    # if there is no exception this block is executed
    print('Block 3')
print('2nd line')
# in this code else is executed

