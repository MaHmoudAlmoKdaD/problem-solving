def matrix_search(matrix, integer):
    col = len(matrix[0]) - 1
    row = 0
    while col >= 0 and row < len(matrix):
        # if integer > matrix[row][col]:
        #     row += 1
        # elif integer < matrix[row][col]:
        #     col -= 1
        # else:
        #     return [row, col]
        if integer == matrix[row][col]:
            return [row, col]
        if integer > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return [-1, -1]
matrix = [
    [1,5,9],
    [2,6,10],
    [3,8,11]
]
print(matrix_search(matrix, 11))
# def a():
#     return 1, 1, 3, 3, 3
# print(a())