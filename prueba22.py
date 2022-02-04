def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        n=n*factorial(n-1)
    return n


fact=factorial(5)

print(fact)