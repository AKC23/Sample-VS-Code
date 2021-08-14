
def is_prime(number):
    if number <= 1:
        return False

# check upto number in range
    for factor in range(2, number): 
        if number % factor == 0:
            return False

    return True


def print_primes(n):
    for number in range(1, n):
        if is_prime(number):
            print('%d is prime' % number)


def main():
    print_primes(42)

if __name__ == "__main__":
    main()
