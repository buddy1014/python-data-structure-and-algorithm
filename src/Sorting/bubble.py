def bubble_sort(unordered_list):
    iteration_size = len(unordered_list) - 1
    for i in range(iteration_size):
        for j in range(iteration_size):
            if unordered_list[j] > unordered_list[j+1]:
                # temp = unordered_list[j]
                # unordered_list[j] = unordered_list[j+1]
                # unordered_list[j+1] = temp
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]

    print(unordered_list)


bubble_sort([4,1,7,3,2,9])