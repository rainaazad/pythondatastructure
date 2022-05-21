# how to find fibonacci number using recursion
def fibonacci_number(n):
    assert n >= 0 and int(n) == n, "fibonacci number cannot be negative number or non integer."
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


print(fibonacci_number(8))


# how to find sum of digits of a positive integer number using
# ex: 10 = 1+0 = 1


def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "number has to be positive only"
    if n == 0:
        return 0
    return int(n % 10) + sum_of_digits(int(n / 10))


print(sum_of_digits(4))


# how to calculate power of a number using recursion


def power(base, exp):
    assert exp >= 0 and int(exp) == exp
    if exp == 0:
        return 1
    return base * power(base, (exp - 1))


print(power(5, 1))


# write a number to find out sum of natural number

def sum_of_natural_number(n):
    if n == 1:
        return 1
    return n + sum_of_natural_number(n - 1)


print(sum_of_natural_number(5))


# how to find gcd (greatest common divisor) of two numbers using recursion?

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'the numbers must be integer only'
    if a < 0:
        return -1 * a
    if b < 0:
        return -1 * b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, 18))


# how to convert a decimal number into a binary number using recursion?

def decimaltobinary(n):
    assert int(n) == n, 'the parameter must be integer only!'
    if n == 0:
        return 0
    return n % 2 + 10 * decimaltobinary(n // 2)


print(decimaltobinary(13))
