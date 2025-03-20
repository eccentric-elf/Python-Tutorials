def prime_factors(n):
    fact = 2
    while n > 1:
        if n % fact == 0:
            print(fact, end=" ")
            n //= fact
        else:
            fact += 1

num = int(input("Enter a number: "))
print("Prime factors:", end=" ")
prime_factors(num)
