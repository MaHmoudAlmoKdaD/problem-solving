# error this code
# reverse = 0
# def reverse_digits(n):
#     global reverse
#     if n > 0:
#         last_digit = n % 10
#         reverse = (reverse * 10) + last_digit
#         reverse_digits(n // 10)
#     return reverse
def reverse_digits(n, reverse=0):
    if n == 0:
        return reverse
    else:
        last_digit = n % 10
        reverse = (reverse * 10) + last_digit
        return reverse_digits(n // 10, reverse)
print(reverse_digits(192))
# print(reverse)