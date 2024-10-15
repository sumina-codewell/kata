n=int(input())
def fibonacci(n):
    if n <= 1:
        return n
     
    if memo[n] is None:
       memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

memo = [None]*100

print(fibonacci(n))