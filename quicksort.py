
# intuition for quicksort: 
'''
Quicksort is a divide-and-conquer recursive approach to sorting an array.
Best case: O(n log n), generalized example: array is randomly sorted
Worst case: O(n^2), generalized example: array is sorted and pivot is the first element

intuition: 
    - pick a pivot (naively, the first element)
    - partition the array into two subarrays:
        - elements less than the pivot
        - elements greater than the pivot
    - recursively apply the above steps to the subarrays
    - base case: subarray with less than 2 elements

If you pick a random pivot, the average time complexity is O(n log n).
'''

def quicksort_naive(array):
    
    # base case: array with 0 or 1 element is already sorted
    if len(array) < 2: 
        return array

    # recursive case:
    else:
        # pick a pivot, naively just the first index
        pivot = array[0]

        # partition the array into two subarrays: 
        left = [val for val in array[1:] if val <= pivot]
        right = [val for val in array[1:] if val > pivot]
    
        # recursively apply the above steps to the subarrays
        return quicksort_naive(left) + [pivot] + quicksort_naive(right)

print(quicksort_naive([2, 3, 26, 6, 2, 3, 8, 9, 45, 34, 23, 17]))