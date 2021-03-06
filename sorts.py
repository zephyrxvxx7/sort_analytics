import logging
from time import clock
from random import randint
from functools import wraps
from copy import deepcopy


# decorator
def time_analytics(func):
    @wraps(func)
    def my_wrap(*args, **kwargs):
        logging.info('Starting {:<15}(N = {:6d})'.format(
            func.__name__, len(*args)))
        t0 = clock()
        func(*args, **kwargs)
        use_time = clock() - t0
        logging.info('Ending   {:<15}(N = {:6d}) in {} sec'.format(
            func.__name__, len(*args), use_time))
        return use_time
    return my_wrap


@time_analytics
def bubble_sort(main_list):

    list_ = deepcopy(main_list)

    for i in range(0, len(list_) - 1):  # 有n-1回合(n為數字個數)
        for j in range(0, len(list_) - 1 - i):  # 每回合進行比較的範圍
            if list_[j] > list_[j + 1]:  # 是否需交換
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


@time_analytics
def insertion_sort(main_list):  # in-place

    list_ = deepcopy(main_list)

    for i in range(1, len(list_)):  # 第一個元素固定，從第二個開始
        temp = list_[i]
        j = i - 1  # 固定元素的前一個數字
        while j >= 0 and temp < list_[j]:
            list_[j + 1] = list_[j]  # 值向右
            j = j - 1
        list_[j + 1] = temp


@time_analytics
def selection_sort(main_list):  # 由小到大 in-place

    list_ = deepcopy(main_list)

    for i in range(0, len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if (list_[min_index] > list_[j]):
                min_index = j

        if (min_index != i):
            list_[min_index], list_[i] = list_[i], list_[min_index]


@time_analytics
def quick_sort(main_list):
    """Source, https://en.wikipedia.org/wiki/Quicksort"""

    list_ = deepcopy(main_list)

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


@time_analytics
def heap_sort(main_list):
    """Source: https://en.wikipedia.org/wiki/Heapsort"""

    list_ = deepcopy(main_list)

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


if __name__ == '__main__':
    #N_list = [50000, 100000, 150000, 200000, 250000, 300000]
    N_list = [300000]
    for N in N_list:
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]
        bubble_sort(randint_list)
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]
        insertion_sort(randint_list)
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]
        selection_sort(randint_list)
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]
        quick_sort(randint_list)
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]
        heap_sort(randint_list)
