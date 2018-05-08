from multiprocessing import cpu_count, Pool
from random import randint
import logging
from copy import copy

import sorts

if __name__ == '__main__':

    N_list = [50000]
    ROUND = 1

    logging.basicConfig(level=logging.INFO)
    pool = Pool(processes=1)

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
'''
    for N in N_list:
        randint_list = [[randint(0, 2 ** 31 - 1)
                         for _ in range(N)] for _ in range(ROUND)]

        for i in range(ROUND):
            bubble_list = copy(randint_list[i])
            insertion_list = copy(randint_list[i])
            selection_list = copy(randint_list[i])
            quick_list = copy(randint_list[i])
            heap_list = copy(randint_list[i])
            pool.apply_async(sorts.bubble_sort, (bubble_list, ))
            pool.apply_async(sorts.insertion_sort, (insertion_list, ))
            pool.apply_async(sorts.selection_sort, (selection_list, ))
            pool.apply_async(sorts.quick_sort, (quick_list, ))
            pool.apply_async(sorts.heap_sort, (heap_list, ))

    pool.close()
    pool.join()
'''
