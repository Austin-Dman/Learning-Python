def num_Gen_N(b,n):
    Nlist=[]
    for x in range(n):
        Nlist.append((x+1)*str(b))
        
    print(Nlist)
    sum=0
    for x in Nlist:
        sum=int(x)+sum
    print(sum)    
    



