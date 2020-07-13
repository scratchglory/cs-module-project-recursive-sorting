# Lecture Artem
# O(N), the function gets called N times
def print_num(n):
    print(n)
    # a base case (i.e the code that tells us to stop running this function)
    if n == 0:
        return

    # recursive case (i.e the case which takes us to the next subproblem)
    print_num(n-1)
    return

# This is a complicated one.. it might seem like n^2 or something similar but:
# Its actually 2^n !!
# (if you want to try verify that, just try this function with 100, and see just how hard your computer chugs)


def double_print_num(n):
    print(n)
    if n == 0:
        return

    double_print_num(n-1)
    double_print_num(n-1)
    return


# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Fib(n) = Fib(n-1) + Fib(n-2)
# Base case:
# at n = 0  Fib(0) == 0
# at n = 1  Fib(1) == 1

# Also 2^N. This implementation of fibonacci is very non-optimal
def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    result = fibonacci(n-1) + fibonacci(n-2)
    return result


print(fibonacci(100))
