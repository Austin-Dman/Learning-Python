
def Value_check(val):
    
    if val.isnumeric():
        print('Value is numeric')
    elif val.isalpha():
        print('Value is alpha')
    elif val.isalnum:
        print('Value is alphanumeric')
    
def is_even(val):
    if (val % 2) ==0:
        return True
    else:
        return False

v = " " 

while v:
    v=str(input('Please type a value to check: '))
    if v=='exit':
        break
    Value_check(v)




