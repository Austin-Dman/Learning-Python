num = input('Please list give your list of numbers seperated by commas: ')

num = list(num.split(','))

num = [int(num) for num in num] #makes list of ints

square_num = [num**2 for num in num if num>10 and num<50] 

print(square_num)