"""Source: https://en.wikipedia.org/wiki/Heapsort"""


def heap_sort(list_):
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
