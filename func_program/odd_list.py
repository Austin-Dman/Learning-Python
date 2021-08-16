x=input('Please type a list of numbers seperated by a comma: ')
x=list(x.split(','))

    
even_list = list(filter(lambda n: int(n) % 2 ==0, x))

if len(even_list) != 0: 
    print('All elements are not odd. ')
else:
    print('All elements are odd. ')