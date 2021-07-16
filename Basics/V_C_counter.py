word = input('Please type a string: ')
C=0
V=0
word=word.lower()


vow = ['a','e','i','o','u']

for x in word:
        for n in vow:
            if x==n:

             V=V+1
            

C=len(word)-V       
print('Amount of vowels: ', V)
print('Number of consonants: ', C )

