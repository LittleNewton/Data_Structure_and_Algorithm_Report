# 4.1.1 The Factorial Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#----------------------------- my main function -----------------------------
print(factorial(10))