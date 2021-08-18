num = input('Please give a list of numbers seperated by commas: ')

even = list(num.split(','))

even = [int(even) for even in even] #makes the list ints

even_list = [even for even in even if even % 2==0]

print(even_list)