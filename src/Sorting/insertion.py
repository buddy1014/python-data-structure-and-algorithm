def insertion_sort(unsorted_list):
    unsorted_list_size = len(unsorted_list)
    for index in range(1, unsorted_list_size):
        search_index = index
        insertion_value = unsorted_list[search_index]

        while search_index > 0 and unsorted_list[search_index-1] > insertion_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1

        unsorted_list[search_index] = insertion_value

    print(unsorted_list)


insertion_sort([1,5,100,2])
    