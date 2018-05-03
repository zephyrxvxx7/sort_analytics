from multiprocessing import cpu_count, Pool
from random import randint
import logging

import sorts

if __name__ == '__main__':

    N_list = [50000, 100000, 150000, 200000, 250000, 300000]

    logging.basicConfig(level=logging.INFO)
    pool = Pool(processes=cpu_count())

    for N in N_list:
        randint_list = [[randint(0, 2 ** 31 - 1)
                         for _ in range(N)] for _ in range(25)]
        for i in range(25):
            pool.apply_async(sorts.bubble_sort, (randint_list[i], ))
            pool.apply_async(sorts.insertion_sort, (randint_list[i], ))
            pool.apply_async(sorts.selection_sort, (randint_list[i], ))
            pool.apply_async(sorts.quick_sort, (randint_list[i], ))
            pool.apply_async(sorts.heap_sort, (randint_list[i], ))

    pool.close()
    pool.join()
