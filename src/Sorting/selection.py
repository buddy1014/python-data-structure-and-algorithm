def selection_sort(unsorted_list):
    unsorted_list_size = len(unsorted_list)

    for i in range(unsorted_list_size):
        for j in range(i+1, unsorted_list_size):
            if unsorted_list[j] < unsorted_list[i]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

    print(unsorted_list)


selection_sort([1, 3, 2, 15, 10])
    