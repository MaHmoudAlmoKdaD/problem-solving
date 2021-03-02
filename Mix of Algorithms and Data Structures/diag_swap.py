def diag_swap(matrix):
    swap_value = len(matrix) - 1
    for i in range((len(matrix) // 2)):
        # swap diagonal from left to right

        value = matrix[i][i]
        matrix[i][i] = matrix[swap_value][swap_value]
        matrix[swap_value][swap_value] = value
        # swap diagonal from right to left

        value = matrix[swap_value][i]
        matrix[swap_value][i] = matrix[i][swap_value]
        matrix[i][swap_value] = value
        swap_value -= 1


if __name__ == '__main__':
    matrix_test = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    diag_swap(matrix_test)
    expected_result = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1]
    ]

    print(matrix_test == expected_result)
