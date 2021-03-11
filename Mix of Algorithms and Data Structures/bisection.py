def bisection(haystack, needable):
    start = 0
    end = len(haystack)
    while start <= end:
        mid = (start + end ) // 2
        if haystack[mid] == needable:
            return mid
        if haystack[mid] > needable:
            end = mid - 1
        else:
            start = mid + 1
    return -1
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bisection(lis, 5))
