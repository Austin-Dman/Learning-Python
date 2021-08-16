import math

def distance_eq(x1,y1,x2,y2):
    
    d= math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d


x1=0    
y1=4
x2=1
y2=5

print(distance_eq(x1,y1,x2,y2))
