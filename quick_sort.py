"""Source, https://en.wikipedia.org/wiki/Quicksort"""


def quick_sort(list_):
    def _quicksort(list_, begin, end):
        # must run partition on sections with 2 elements or more
        if begin < end:
            p = partition(list_, begin, end)
            _quicksort(list_, begin, p)
            _quicksort(list_, p+1, end)

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
    _quicksort(list_, 0, len(list_)-1)
    return list_
