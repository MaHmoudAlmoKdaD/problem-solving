# def fib(n):
#
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(232))
# def fib(n):
#     initial = 0
#     last = 0
#     def fib_internal(n, to_stop, last):
#
#         if n == to_stop:
#             return n
#         first = initial + fib_internal(n, to_stop + 1, last)
#         last += first
#         return last
#     return fib_internal(n, 0, last)
def fibonacci(n):
    first, last, total = 0, 1, 0
    if n == 0 or n == 1:
        return 0
    if (n == 2):
        return 1
    for i in range(1, n):
        first = last
        last = total
        total = first + last
    return total
print(fibonacci(5))