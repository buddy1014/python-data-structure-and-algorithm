# list should be sorted first, then we can apply this algorithm to the list
def binary_search(ordered_list, term):
    size_of_list = len(ordered_list)

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2

        if ordered_list[mid_point] == term:
            return mid_point
        
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
    
    if index_of_first_element > index_of_last_element:
        return None
    

def recursive_binary_search(ordered_list, first_element_index, last_element_index, term):
    if first_element_index > last_element_index:
        return None
    else:
        mid_point = first_element_index + (last_element_index - first_element_index) // 2

        if ordered_list[mid_point] > term:
            return recursive_binary_search(ordered_list, first_element_index, mid_point-1, term)
        elif ordered_list[mid_point] < term:
            return recursive_binary_search(ordered_list, mid_point+1, last_element_index, term)
        else:
            return mid_point
        

# example
store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search(store, 2))
