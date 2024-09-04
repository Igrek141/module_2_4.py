numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(2, len(numbers) + 1):
    sum_ = 0
    for j in range(2, i + 1):
        b = i % j
        if b == 0:
            sum_ += 1
    if sum_ == 1:
        is_prime = True
        primes.append(i)
    else:
        is_prime = False
        not_primes.append(i)
print('Primes:    ', primes)
print('Not Primes:', not_primes)