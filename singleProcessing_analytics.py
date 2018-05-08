from random import randint
import logging
from copy import copy

import sorts

if __name__ == '__main__':

    N_list = [50000]
    ROUND = 1

    logging.basicConfig(level=logging.INFO)

    for N in N_list:
        randint_list = [[randint(0, 2 ** 31 - 1)
                         for _ in range(N)] for _ in range(ROUND)]

        for i in range(ROUND):
            bubble_list = copy(randint_list[i])
            insertion_list = copy(randint_list[i])
            selection_list = copy(randint_list[i])
            quick_list = copy(randint_list[i])
            heap_list = copy(randint_list[i])

            sorts.bubble_sort(bubble_list)
            sorts.insertion_sort(insertion_list)
            sorts.selection_sort(selection_list)
            sorts.quick_sort(quick_list)
            sorts.heap_sort(heap_list)
