# lecture Artem
import time

# O(N)


def partition(numbers):
    # this function breaks numbers into a left, pivot and right
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


# O(N Log N) -> We run partition (which is O(N)) aproximately Log(n) times
def quicksort(numbers):
    # base case
    # what is the easiest array to sort?
    # "Conquer" step, its just so easy
    if len(numbers) <= 1:
        return numbers

    # divide
    # figure out how to properly split our data
    left, pivot, right = partition(numbers)

    sorted_array = quicksort(left) + [pivot] + quicksort(right)
    return sorted_array


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
