# Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number, and False otherwise.

def is_prime(number):
    if number in range(2, 1001):
        return True
    return False

# print(is_prime(1001))
