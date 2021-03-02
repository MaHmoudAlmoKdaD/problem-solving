#clousre
def factorial(n):
    def factorial_internal(n):
        if (n == 1) or (n == 0):
            return 1
        return n * factorial(n - 1)
    if n < 0:
        raise TypeError('factorial undefined for negative number')
    return factorial_internal(n)


print(factorial(5))