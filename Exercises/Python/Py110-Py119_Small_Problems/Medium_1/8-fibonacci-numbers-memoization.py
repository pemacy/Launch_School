'''
Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed. In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

An image representing the computation of the 7th Fibonacci number is shown below. It is the same image that was shown in the previous exercise, except this one highlights the values that have previously been computed.
'''

fib = {1: 1, 2: 1}

def fibonacci(n):
    if fib.get(n):
        return fib[n]
    else:
        fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib[n]

'''
print(fibonacci(1))# == 1)                  # True
print(fibonacci(2))# == 1)                  # True
print(fibonacci(3))# == 2)                  # True
print(fibonacci(4))# == 3)                  # True
print(fibonacci(5))# == 5)                  # True
print(fibonacci(6))# == 8)                  # True
print(fibonacci(12))# == 144)               # True
print(fibonacci(20))# == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
'''
