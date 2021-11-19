def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
    
for i in range(0, 6):
    print(i, factorial_function(i))