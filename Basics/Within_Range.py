range_num = input('Please enter start and end of range, your variance, and the value you wish to check (values should be seperated by commas): ')

range_num=range_num.split(',')

start=int(range_num[0])
end=int(range_num[1])
var=int(range_num[2])
num=int(range_num[3])


def Range_Check(start, end, variance, num):
    start=start-variance
    end=end+variance
    if start<=num and end>=num:
        print('Number is with/within variance of range limits')
    else:
        print('Number is not within varience of range limits')

Range_Check(start,end,var,num)
