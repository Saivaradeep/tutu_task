def factorial(n):
    if n<2:
        return 1
    else:
        a= n*factorial(n-1)
        return a
result=factorial(5)
print(result)
    
    
