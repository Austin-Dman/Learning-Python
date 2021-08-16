x=list(range(1,11))

even_check = lambda n: n % 2 ==0

even_list = list(filter(even_check, x))

print('Even numbers found: ',even_list)
