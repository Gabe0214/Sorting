# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    merged = []

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-
    # If the array is empty or length 1, return

    length = len(arr)
    middle_index = length // 2
    first_half = merge_sort(arr[:middle_index])
    second_half = merge(arr[middle_index:])

    if len(arr) <= 1:
        return arr

    return merge(first_half, second_half)


items = [2, 8, 9, 4, 1, 6, 22, 15, 32, 55, 89, 124, 300, 8]
length = len(items)
middle_index = length // 2

# print(items[:middle_index])
# print(items[middle_index:])
print(merge_sort(items))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
