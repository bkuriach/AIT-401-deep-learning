# Approach 1
'''
Recursion.
Complexity: O(n)
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Approach 2
'''
For loop.
Complexity: O(n)
'''
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))
