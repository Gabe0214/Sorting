# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        #print(arr[i])
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                # print(arr[smallest_index])

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # TO-DO: swap



    return arr


num = [8, 1, 9, 4, 12, 32, 15, 7, 55, 100, 11, 3]



selection_sort(num)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range( len(arr) - 1):
        # length of the list  - 1 because the last item is not iterable.

        for j in range( len(arr) -1):
            # make a nested for loop
            #print(arr)
            if arr[j] > arr[j+1]: # if the current index is greater than the index next to it, swap them.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


num_2 = [25, 12, 7, 2, 36, 55, 18, 22]

print(bubble_sort(num_2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr