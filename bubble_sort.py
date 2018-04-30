def bubble_sort(list_):
    for i in range(0, len(list_) - 1):  # 有n-1回合(n為數字個數)
        for j in range(0, len(list_) - 1 - i):  # 每回合進行比較的範圍
            if list_[j] > list_[j + 1]:  # 是否需交換
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_
