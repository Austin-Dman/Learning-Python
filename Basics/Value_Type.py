
def Value_check(val):
    
    if val.isnumeric():
        print('Value is numeric')
    elif val.isalpha():
        print('Value is alpha')
    elif val.isalnum:
        print('Value is alphanumeric')
    
        

v = " " 

while v:
   
    v=str(input('Please type a value to check: '))
    if v=='exit':
        break
    Value_check(v)


