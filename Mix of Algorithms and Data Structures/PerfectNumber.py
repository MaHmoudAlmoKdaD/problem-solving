def perfect(number):
    sum = 0
    isPerfect = False
    stride = 2 if number % 2 != 0 else 1
    for i in range(1, number, stride):
        if (number % i == 0):
            sum += i
    if(sum == number):
        isPerfect = True
    return isPerfect
print(perfect(6))