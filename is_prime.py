def is_prime(n):
    """is_prime is a function that checks if the entered number n is a prime number."""
    if n <= 1:
        return print(f"{n} is not a prime number.")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return print(f"{n} is not a prime number.")
    return print(f"{n} is a prime number.")

is_prime(29)
is_prime(28)
is_prime(39)
is_prime(199)
