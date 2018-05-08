from random import randint
import logging
from copy import copy

import sorts

if __name__ == '__main__':

    N_list = [50000]
    ROUND = 1

    logging.basicConfig(level=logging.INFO)

    #N_list = [300000]
    for N in N_list:
        randint_list = [randint(0, 2 ** 31 - 1) for _ in range(N)]

        bubble_list = copy(randint_list)
        insertion_list = copy(randint_list)
        selection_list = copy(randint_list)
        quick_list = copy(randint_list)
        heap_list = copy(randint_list)

        sorts.bubble_sort(bubble_list)
        sorts.insertion_sort(insertion_list)
        sorts.selection_sort(selection_list)
        sorts.quick_sort(quick_list)
        sorts.heap_sort(heap_list)
