import logging
from time import clock


# decorator
def time_analytics(func):
    def my_wrap(*args, **kwargs):
        logging.info('Starting {0}(N = {1})'.format(func.__name__, len(*args)))
        t0 = clock()
        func(*args, **kwargs)
        logging.info('Ending {0}(N = {1}) in {2} sec'.format(
            func.__name__, len(*args), clock() - t0))
    return my_wrap


@time_analytics
def bubble_sort(list_):
    for i in range(0, len(list_) - 1):  # 有n-1回合(n為數字個數)
        for j in range(0, len(list_) - 1 - i):  # 每回合進行比較的範圍
            if list_[j] > list_[j + 1]:  # 是否需交換
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


@time_analytics
def insertion_sort(list_):  # in-place
    for i in range(1, len(list_)):  # 第一個元素固定，從第二個開始
        temp = list_[i]
        j = i - 1  # 固定元素的前一個數字
        while j >= 0 and temp < list_[j]:
            list_[j + 1] = list_[j]  # 值向右
            j = j - 1
        list_[j + 1] = temp
    return list_


@time_analytics
def selection_sort(list_):  # 由小到大 in-place
    for i in range(0, len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if (list_[min_index] > list_[j]):
                min_index = j

        if (min_index != i):
            list_[min_index], list_[i] = list_[i], list_[min_index]

    return list_


@time_analytics
def quick_sort(list_):
    """Source, https://en.wikipedia.org/wiki/Quicksort"""

    def _quicksort(list_, begin, end):
        # must run partition on sections with 2 elements or more
        if begin < end:
            p = partition(list_, begin, end)
            _quicksort(list_, begin, p)
            _quicksort(list_, p + 1, end)

    def partition(list_, begin, end):
        pivot = list_[begin]
        while True:
            while list_[begin] < pivot:
                begin += 1
            while list_[end] > pivot:
                end -= 1
            if begin >= end:
                return end
            list_[begin], list_[end] = list_[end], list_[begin]
            begin += 1
            end -= 1
    _quicksort(list_, 0, len(list_) - 1)
    return list_


@time_analytics
def heap_sort(list_):
    """Source: https://en.wikipedia.org/wiki/Heapsort"""

    def heapify(begin, end):
        """最大堆調整"""
        root = begin
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and list_[child] < list_[child + 1]:
                child += 1
            if list_[root] < list_[child]:
                list_[root], list_[child] = list_[child], list_[root]
                root = child
            else:
                break

    # Max Heap
    for begin in range((len(list_) - 2) // 2, -1, -1):
        heapify(begin, len(list_) - 1)

    # Heap sort
    for end in range(len(list_) - 1, 0, -1):
        list_[0], list_[end] = list_[end], list_[0]
        heapify(0, end - 1)
    return list_
