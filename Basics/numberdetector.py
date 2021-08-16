def num_flag(x):
    nums=[1,2,3,4,5,6,7,8,9,0]
    for i in x:

        if int(i) in nums:
            nums.remove(int(i))
    return nums







x = input("Please enter a number: ")

print(num_flag(x))