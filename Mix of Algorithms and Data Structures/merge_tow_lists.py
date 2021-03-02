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
l1 = [11,12,54,73,911]
l2 = [21, 30, 62, 110]
print(merge(l1, l2))