def sertion_sort(l):

    for i in range(1, len(l)):
        value = l[i]
        last_sorted_index = i - 1
        while value < l[last_sorted_index] and last_sorted_index >= 0:
            l[last_sorted_index + 1] = l[last_sorted_index]
            last_sorted_index = last_sorted_index - 1
        l[last_sorted_index + 1] = value

    return l


l = [1, 5, -2, -3]
print(sertion_sort(l))