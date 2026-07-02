b=2
e=4

def pot(b,e):
    if b==0:
        return 0
    if e==0:
        return 1
    else:
        return b*pot(b,e-1)  
    
print(pot(b,e))