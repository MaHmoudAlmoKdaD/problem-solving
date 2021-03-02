# def recursive_sum(n):
#     l = [-1] * (n+1)
#     def sum_internal(n):
#         if n <= 1:
#            return n
#         if l[n] == -1:
#             print(l)
#             l[n] = n + sum_internal(n-1)
#         # return l[n] + sum_internal(n-1)
#     return sum_internal(n)
#
def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n - 1)

print(recursive_sum(3))
# sum = 3+2
# 3+2