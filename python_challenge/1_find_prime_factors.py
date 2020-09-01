# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

# "Factors" are the numbers you multiply together to get another number

# "Prime Factorization" is finding which prime numbers multiply together to make the original number.

def get_prime_factors(n):
    prime_factors = list()
    divisor = 2
    while divisor <= n:
        if (n % divisor) == 0:
            prime_factors.append(divisor)
            n = n/divisor
        else:
            divisor += 1
    for i in range(len(prime_factors)): 
        print(prime_factors[i]),


if __name__ == '__main__':
    print(get_prime_factors(630))
    

# 2 3 3 5 7
# 2*3*3*5*7 = 630