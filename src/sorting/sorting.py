# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements  # a way to create a list of 0s
    # mergaed_arr = [0 for _ in range(elements)] # list comprehensions

    # must sort arrA and has to equal arrB
    # start pointers at the start of both lists
    a, b = 0, 0  # initialize pointers

    # traverse both pointers through their respective lists
    # loop through our merged_arr
    for i in range(len(merged_arr)):
        # check if a pointer is out of bounds of its repective array
        # if it is, then we jus tneed to copy over every element from the other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # both indices are still in bounds of their respective arrays
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        # compare the vlaues at both pointers

        # whichever value is smaller, we copy that value to our merged list
        # increment that pointer

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # phase 1: keep splitting our arr until we have lists of length 1
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])  # half way
        right = merge_sort(arr[len(arr) // 2:])  # to the end
        # phase 2: building those lists make up by using our 'merge' function
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
