'''This module contains sorting function, which are currently working with INT and FLOAT list types.'''
from random import randint


def create_random_int_array(size, min_value=0, max_value=1000):
    '''Creating array to sort with random integer values.
    By default, it fills in values in a range from 0 to 1000, 
    however you can change these by inputting min_value and max_value parameters.'''
    return [randint(min_value,max_value) for _ in range(0, size-1)]


def create_random_str_array(size):
    '''Creating array to sort with random str values.'''
    return [chr(randint(0,256)) for _ in range(0, size-1)]


def print_arr(arr, type, time_p):   
    '''Representation of an array'''
    str_arr = f"{type}: "
    if len(arr) < 15:
        return arr
    else:
        str_arr += "["
        for num in arr[:3]:
            str_arr += str(num) + ', '
        
        str_arr += " ... "

        for num in arr[len(arr)-3:]:
            str_arr += ', ' + str(num) 
        
        str_arr += "]\n"

    if time_p != 0:
        str_arr += f"Time passed: {time_p}\n"

    return print(str_arr)

# Bubblesort      
def bubble_sort(arr):
    '''Worst and average case: O(n^2)
    This algorithm is not used in practice.'''
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                c = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = c
    return arr


# Insertionsort
def insertion_sort(arr):
    '''Insertionsort has a time complexity of O(n^2) in the worst and average case, 
    and O(n) in the best case (if the array is already sorted). 
    It's useful for small data sets or when the data is mostly sorted.'''
        # Starting from second element
    for i in range(1, len(arr)):
        key = arr[i]
        # Setting j to previous element
        j = i-1
        # If key is less than previous element, we are moving the array elements forward until we will reach smaller number
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # Inserting key into its place
        arr[j+1] = key
    return arr


# Selectionsort
def selection_sort(arr):   
    '''Selectionsort has a time complexity of O(n^2) in the worst and average case. 
    This algorithm is not used in practice as it is only good for smaller arrays.'''
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Quicksort
def partition(arr, low, high): 
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    '''The average time complexity of quicksort is O(n log n) but in worst case it can be O(n^2)'''
    if low < high:
        pivot_index = partition(arr, low, high)
        # Recursively sorting 2 sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr


def merge_sort(arr):
    '''Mergesort has a time complexity of O(n log n) in the worst and average case, 
    making it a good choice for large data sets.'''
    if len(arr) <= 1:
        return arr
    
    # // returns floor value if float created upon division
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively keep on merging each half
    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0

    # Merge the sorted halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    # Add remaining elements
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr


# Heapsort
def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
def heap_sort(arr): 
    '''Heapsort has a time complexity of O(n log n) in the worst and average case.
    It is not a stable sort.'''
    n = len(arr)
  
    for i in range(n, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
  
    return arr

 
# Countingsort
def counting_sort(arr):
    '''It has a time complexity of O(n + k) where k is the range of the input. 
    It's efficient for sorting large numbers of integers with a small range.'''
    if len(arr) == 0:
        return []

    max_element = max(arr)
    count = [0] * (max_element + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    output_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output_arr

def counting_sort_str(arr):
    '''This algorithm is best suited for sorting elements that have a small range of possible values. 
    In the case of ASCII symbols, there are only 256 possible values.'''
    # Create a count array to store the count of each character
    count = [0] * 256
    for i in arr:
        count[ord(i)] += 1 # ord(i) returns number of symbol in unicode

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    output = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    return output