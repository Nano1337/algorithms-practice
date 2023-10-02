
array = [2, 3, 26, 6, 2, 3, 8, 9, 45, 34, 23, 17]

def selection_sort(array): 
    
    # iterate through each starting point in the array 
    for i in range(len(array)): 
        
        # initialize the minimum value to the starting point
        min_value = i

        # iterate through the array starting at the next index
        for j in range(i+1, len(array)):
            
            # check if the current value is less than the minimum value
            if array[j] < array[min_value]:
                
                # if so, update the minimum value index
                min_value = j

        # swap the minimum value with the starting point
        array[i], array[min_value] = array[min_value], array[i]

    return array

# Basically tries to find the smallest value in the array and finally swaps it with the outer loop index
# Time Complexity: O(n^2) - nested for loops

print(selection_sort(array))