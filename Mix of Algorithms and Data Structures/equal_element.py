def equal_elements(M):
    dictionary = {}
    for k in range(len(M)):
        for j in range(len(M[k])):
            if M[k][j] in dictionary:
                list_points = (dictionary.get(M[k][j]), (k, j))
                return list_points
            dictionary[M[k][j]] = (k, j)
    return (-1, -1), (-1, -1)


M1 = [[1, 2], [3, 4]]
M2 = [[1, 2], [3, 1]]
M3 = [[1, 3, 0, 5], [2, 5, 2, -1], [5, 6, -2, 6]]
M4 = [[1, 12, 0, 5], [20, 50, 121, -1], [11, 31, 2]]
# for M in (M1, M2, M3, M4):
#     print(equalElements(M), "\n")
# ((-1, -1), (-1, -1))
# ((0, 0), (1, 1))
# ((0, 3), (1, 1))
# ((-1, -1), (-1, -1))

print(equal_elements(M4))
