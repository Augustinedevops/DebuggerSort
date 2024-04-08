def quicksort(array):
    if len(array) <= 1:
        return array
    pivot_element = array[len(array) // 2]
    smaller_elements = []
    equal_elements = []
    greater_elements = []
    for element in array:
        if element < pivot_element:
            smaller_elements.append(element)
        elif element == pivot_element:
            equal_elements.append(element)
        else:
            greater_elements.append(element)
    print('Partitioned arrays:', smaller_elements, equal_elements, greater_elements)
    sorted_array = quicksort(smaller_elements) + equal_elements + quicksort(greater_elements)
    return sorted_array
unsorted_array = [5, 4, 2, 1, 3]
print('Unsorted array:', unsorted_array)
sorted_array = quicksort(unsorted_array)
print('Sorted array:', sorted_array)