def addition(n):
    if n==0:
        return 0

    return n + addition(n-1)
                        
a = addition(7)    
print(a)