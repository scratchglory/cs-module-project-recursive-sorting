# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    if low > high:
        return - 1  # not found
    else:
        mid = (low + high) // 2  # find the midpoint
        # check our array mid matches target
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # toss out right side
            # recurse
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid+1, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
