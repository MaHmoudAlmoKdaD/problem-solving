def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[mid:])
    right = merge_sort(l[:mid])
    return merge(left, right)
def merge(l1, l2):
    i, j = 0, 0
    l3 = list()
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    return l3 + l2[j:] + l1[i:]
l = [17, -1, 4, 6]
print(merge_sort(l))