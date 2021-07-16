first_name = input('Please enter your first name. ')
Last_name = input("Now enter your last name. ")

for i in first_name,Last_name:
   reverseF=first_name[::-1]
   reverseL=Last_name[::-1]

print("Here is your name backwards: {} {}".format(reverseF,reverseL))