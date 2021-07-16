word=input('Please enter your word of choice: ')

word=word.lower()
A_V=0
E_V=0
I_V=0
O_V=0
U_V=0

for x in word: 
    if x=='a':
        A_V+=1
    if x=='e':
        E_V+=1
    if x=='i':
        I_V+=1
    if x=='o':
        O_V+=1
    if x=='u':
        U_V+=1

print('Amount of vowel a: ', A_V)

print('Amount of vowel e: ', E_V)

print('Amount of vowel i: ', I_V)

print('Amount of vowel o: ', O_V)

print('Amount of vowel u: ', U_V)