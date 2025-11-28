# Factorial of a number
num = int(input("Enter the number : "))

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

ans = fact(num)
print(f'Factorial of {num} is : ',ans)

# Fibonaci Series
num1 = int(input("Enter the number : "))

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

ans1 = fib(num1)
print(f'Fibonaci series : ',ans1)