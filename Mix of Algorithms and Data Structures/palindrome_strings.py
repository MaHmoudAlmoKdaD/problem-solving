
def palindrome(input_str):
    string = ''
    #     for i in range(len(input_str) - 1, -1, -1):
    #         string += input_str[i]
    #     if string == input_str:
    #         return True
    #     else:
    #         return False
    #------------
    #ANOTHER SOLVE
    # start = 0
    # end = len(input_str) - 1
    # while start < end:
    #     if input_str[start] != input_str[end]:
    #         return False
    #     start += 1
    #     end -= 1
    # return True
    #____________________
#     ANOTHER SOLVE
    for start in range(len(input_str) // 2):
        end = len(input_str) - 1 - start
        if input_str[start] != input_str[end]:
            return False
    return True
def max_sub_palindrome(input_str):
    is_palindrome = ''
    for i in range(len(input_str)):

        for j in range(i + 1, len(input_str) + 1):
            if j - i < len(is_palindrome):
                continue
            substr = input_str[i: j]
            if  len(substr) > len(is_palindrome) and palindrome(substr) :
                is_palindrome = substr
    return is_palindrome
print(max_sub_palindrome('abe'))
