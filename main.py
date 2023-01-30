from copy import deepcopy
import time
import sort_algorithms as srt

# 500 elements is not enough to see difference between good sorting algorithms,
# however you can see the improvement over simple ones like bubble and selection.   
arr_int = srt.create_random_int_array(1000)
srt.print_arr(arr_int, "Unsorted ints", 0)

arr_str = srt.create_random_str_array(1000)
srt.print_arr(arr_str, "Unsorted ASCII", 0)

bubble_arr = deepcopy(arr_int)
start_t = time.time()
bubble_arr = srt.bubble_sort(bubble_arr)
time_passed = '{:.10f}'.format(time.time() - start_t)
srt.print_arr(bubble_arr, "Bubblesirt", time_passed)

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