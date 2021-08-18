list1 = input('Please enter your elements for list 1, seperated by commas: ')
list2 = input('Please enter your elements for list 2, seperated by commas: ')

list1 = list(list1.split(','))
list2 = list(list2.split(','))
new_list = [ (x,y) for x in list1 for y in list2]

print(new_list)