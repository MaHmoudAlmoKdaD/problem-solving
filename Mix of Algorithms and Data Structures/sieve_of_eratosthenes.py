def sieve_of_eratosthenes(n):
    prime_list = [True] * (n + 1)
    for i in range(2, int(n ** (1 / 2)), 1):
        if prime_list[i]:
            for j in range(i ** 2, n + 1, i):
                prime_list[j] = False

    final_primes = []
    for i in range(2, len(prime_list)):
        if prime_list[i]:
            final_primes.append(i)
    return final_primes
#------------------------
#ANOTHER SOLUTION
    # if n <= 1 :
    #     return None
    # elif n == 2:
    #     return 2
    # else:
    #     l_numbers = [num for num in range(2, n + 1)]
    #     for prime in l_numbers:
    #         for number in range(prime, n + 1):
    #             if (prime * number) in l_numbers:
    #                 l_numbers.remove(prime * number)
    # return l_numbers



print(sieve_of_eratosthenes(100))