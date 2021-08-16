x=list(range(1,21))

square = list(map(lambda n: n**2,x))

limit_list=list(filter(lambda n: n>10 and n<50 ,square))

print(limit_list)