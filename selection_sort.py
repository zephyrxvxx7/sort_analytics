def selection_sort(list_):  # 由小到大 in-place
    for i in range(0, len(list_)-1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if (list_[min_index] > list_[j]):
                min_index = j

        if (min_index != i):
            list_[min_index], list_[i] = list_[i], list_[min_index]

    return list_
