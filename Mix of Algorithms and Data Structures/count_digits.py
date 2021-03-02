def count_digits(n):
    length = len(str(n))
    number = 1
    def count_internal(length):
        if n == 0:
            return 0
        elif length == number:
            return 1
        return number + count_internal(length - 1)
    return count_internal(length)
print(count_digits(0))