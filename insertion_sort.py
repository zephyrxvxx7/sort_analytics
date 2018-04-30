def insertion_sort(list_):  # in-place
    for i in range(1, len(list_)):  # 第一個元素固定，從第二個開始
        temp = list_[i]
        j = i - 1  # 固定元素的前一個數字
        while j >= 0 and temp < list_[j]:
            list_[j + 1] = list_[j]  # 值向右
            j = j - 1
        list_[j + 1] = temp
    return list_
