num_list = input('Please enter your values for the histogram, seperated by commas: ')

num_list = list(num_list.split(','))
num_list = [int(num_list) for num_list in num_list]

histograph = [ print('#'*num_list) for num_list in num_list]



