# def cubic_root(n):
#     for i in range(0, n+1):
#         if ((i ** 3) == n):
#             print('{}, exact!'.format(i))
#             break
#         elif ((i ** 3) > n):
#             print('{}, not exact with difference {}'.format(i - 1, n - ((i - 1) ** 3)))
#             break
#
#
def cubic_root(n):
    start = 0
    end = n
    mid = (start + end) // 2
    number = mid ** 3
    while True:
        if n == 1 or n == 0:
            print('{}, exact!'.format(n))
            break
        if (number == n):
            print('{}, exact!'.format(mid))
            break
        elif number < n:
            start = mid
            mid = (start + end) // 2
            number = mid ** 3
            print(start, mid, end)
            if (start == mid):
                print('{}, not exact with difference {}'.format(mid, (n - number)))
                break
        else:
            end = mid
            mid = (start + mid) // 2
            number = mid ** 3
            print(start, mid, end)
cubic_root(99)
# def diff(n, mid):
#     if (n > (mid * mid * mid)):
#         return (n - (mid * mid * mid))
#     else:
#         return ((mid * mid * mid) - n)
#
#     # Returns cube root of a no n
#
#
# def cubicRoot(n):
#     # Set start and end for binary
#     # search
#     start = 0
#     end = n
#
#     # Set precision
#     e = 0.0000001
#     while (True):
#
#         mid = (start + end) // 2
#         error = diff(n, mid)
#
#         # If error is less than e
#         # then mid is our answer
#         # so return mid
#         if (error <= e):
#             return mid
#
#             # If mid*mid*mid is greater
#         # than n set end = mid
#         if ((mid * mid * mid) > n):
#             end = mid
#
#             # If mid*mid*mid is less
#         # than n set start = mid
#         else:
#             start = mid
#
#         # Driver code
#
#
# n = 30
# print("Cubic root of", n, "is",
#       round(cubicRoot(n), 6))