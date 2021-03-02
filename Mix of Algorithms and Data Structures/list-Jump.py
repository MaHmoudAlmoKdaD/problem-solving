def list_jumps(jumps):
    k = 0
    # next_index = 0
    jump = k + jumps[k]
    while jump < len(jumps) and jump >= 0:
        # last = jump + jumps[jump]
        if jump + jumps[jump] == k:
            return 'cycle'
        k = jump
        jump = k + jumps[k]
    return 'out-of-bounds'
# ===================================
# ANOTHER SOLUTION
#     k = 0
#     l = []
#     while k < len(jumps) and k >= 0:
#         if k in l:
#             return 'cycle'
#         l.append(k)
#         k = k + jumps[k]
#     return 'out-of-bounds'


l = [1, 1, 4, 3,2,-5]
print(list_jumps(l))