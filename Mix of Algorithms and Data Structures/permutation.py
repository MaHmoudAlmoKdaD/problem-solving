# def is_permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     # l_str = [i for i in str1]
#     # for i in str2:
#     #     if i not in l_str:
#     #         return False
#     # return True
# # ANOTHER SOLUTION
#     string1 = sorted(str1)
#     string2 = sorted(str2)
#     if string1 == string2:
#         return True
#     return False
#
# def get_permutation_list(input_str, output_str):
#     list_input_str = [i for i in input_str]
#     indices_list = list()
#     for i in output_str:
#         if i in list_input_str:
#             index = list_input_str.index(i)
#             list_input_str[index] = False
#             indices_list.append(index)
#     return indices_list


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    char_dict = {}
    for char in str1:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    for char in str2:
        if char not in char_dict or char_dict[char] == 0:
            return False
        char_dict[char] -= 1

    return True

def get_permutation_list(input_str, output_str):

    index_dictionary = {}
    for index in range(len(input_str)):
        if index not in index_dictionary:
            index_dictionary[input_str[index]] = []
        index_dictionary[input_str[index]].append(index)
    premutation_list = []
    for char in output_str:
        premutation_list.append(index_dictionary[char].pop(0))
    return premutation_list
print(is_permutation('assf', 'fssa'))
print(get_permutation_list("123","231"))