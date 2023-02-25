# Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number, and False otherwise.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = 20  # check any numbers

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
