from copy import deepcopy
import time
import sort_algorithms as srt

running = True
print(f"Sorting algorithms testing unit.")
while running:

    try:
        int_size = int(input("Input size of an numbers list, enter 0 to skip: "))
    except ValueError:
        size_given = False
        while not size_given:
            try:
                int_size = int(input("Incorrect size value, try whole values, i.e. 1000: "))
                size_given = True
            except:
                continue

    try:     
        str_size = int(input("Input size of an characters list, enter 0 to skip: "))
    except ValueError:
        size_given = False
        while not size_given:
            try:
                str_size = int(input("Incorrect size value, try whole values, i.e. 1000: "))
                size_given = True
            except:
                continue

    arr_int = srt.create_random_int_array(int_size, 0, 100000)
    srt.print_arr(arr_int, "Unsorted ints")

    arr_str = srt.create_random_str_array(str_size)
    srt.print_arr(arr_str, "Unsorted ASCII")

    if len(arr_int)>0:
        print("Sorting numbers.")
        bubble_arr = deepcopy(arr_int)
        start_t = time.time()
        bubble_arr = srt.bubble_sort(bubble_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(bubble_arr, "Bubblesort", time_passed)

        insertion_arr = deepcopy(arr_int)
        start_t = time.time()
        insertion_arr = srt.insertion_sort(insertion_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(insertion_arr, "Insertionsort", time_passed)

        selection_arr = deepcopy(arr_int)
        start_t = time.time()
        selection_arr = srt.selection_sort(selection_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(selection_arr, "Selectionsort", time_passed)

        quick_arr = deepcopy(arr_int)
        start_t = time.time()
        quick_arr = srt.quick_sort(quick_arr, 0, len(quick_arr)-1)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(quick_arr, "Quicksort", time_passed)

        merge_arr = deepcopy(arr_int)
        start_t = time.time()
        merge_arr = srt.merge_sort(merge_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(merge_arr, "Mergesort", time_passed)

        heap_arr = deepcopy(arr_int)
        start_t = time.time()
        heap_arr = srt.heap_sort(heap_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(heap_arr, "Heapsort", time_passed)

        counting_arr = deepcopy(arr_int)
        start_t = time.time()
        counting_arr = srt.counting_sort(counting_arr)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(counting_arr, "Countingsort", time_passed)

    if len(arr_str) > 0:
        print("Sorting characters.")
        counting_arr_str = deepcopy(arr_str)
        srt.print_arr(counting_arr_str, "Unsorted")
        start_t = time.time()
        counting_arr_str = srt.counting_sort_str(counting_arr_str)
        time_passed = '{:.10f}'.format(time.time() - start_t)
        srt.print_arr(counting_arr_str, "Countingsort", time_passed)

    cont_unit = input("Continue testing? 'y' or 'n':").lower()
    while not (cont_unit == 'y' or cont_unit == 'n'):
        cont_unit = input("Incorrect input. Try again: ")

    if cont_unit == 'n':
        running = False