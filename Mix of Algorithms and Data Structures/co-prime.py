# def coprime(a, b):
#     is_coprime = 1
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             is_coprime = i
#     return is_coprime == 1
# def coprime2(a, b):
#     low = min(a, b)
#     if a % 2 == 0 and b == 2:
#         return False
#     for i in range(3, low + 1, 2):
#         if a % i == 0 and b % i == 0:
#             return False
#     return True
# # euclidean algorthim? tell us if the numbers is GCD
# def coprime1(a, b):
#     def gcd(a, b):
#         while b != 0:
#             a, b = b, a % b
#         return a == 1
#     return gcd(a, b)
#
# def count_coprimes(n):
#     count = 0
#     for i in range(1, n + 1):
#         if coprime1(n, i):
#             count += 1
#     return count
def coprime(a, b):
    def gcd(a,b):
        while b!=0:
            a=b
            b=a%b
        return a
    return gcd(a,b) ==1
def count_coprimes(n):
    count = 0
    for i in range(1,n):
        if coprime(i,n):
            count = count + 1
    return count
print(coprime(12,100))