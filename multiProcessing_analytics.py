from multiprocessing import cpu_count, Pool
from random import randint
import logging
from copy import copy, deepcopy
from time import clock

import sorts
from result_output import draw_figure, write_xlxs

if __name__ == '__main__':
    t0 = clock()

    N_list = [5000, 10000, 15000]
    ROUND = 3

    logging.basicConfig(level=logging.INFO)
    pool = Pool(processes=8)

    results_list = []
    for N in N_list:
        randint_list = [[randint(0, 2 ** 31 - 1)
                         for _ in range(N)] for _ in range(ROUND)]

        for i in range(ROUND):
            results_list.append(pool.apply_async(
                sorts.bubble_sort, (randint_list[i], )))
            results_list.append(pool.apply_async(
                sorts.insertion_sort, (randint_list[i], )))
            results_list.append(pool.apply_async(
                sorts.selection_sort, (randint_list[i], )))
            results_list.append(pool.apply_async(
                sorts.quick_sort, (randint_list[i], )))
            results_list.append(pool.apply_async(
                sorts.heap_sort, (randint_list[i], )))

    pool.close()
    pool.join()

    use_time = clock() - t0
    print('Total used time: {}'.format(use_time))

    N_list_dict = {N: [] for N in N_list}

    results_dict = {'Bubble Sort': deepcopy(N_list_dict),
                    'Insertion Sort': deepcopy(N_list_dict),
                    'Selection Sort': deepcopy(N_list_dict),
                    'Quick Sort': deepcopy(N_list_dict),
                    'Heap Sort': deepcopy(N_list_dict)
                    }
    count = 0
    for N in N_list:
        for i in range(ROUND):
            results_dict['Bubble Sort'][N].append(
                results_list[count].get())

            results_dict['Insertion Sort'][N].append(
                results_list[count + 1].get())
            results_dict['Selection Sort'][N].append(
                results_list[count + 2].get())
            results_dict['Quick Sort'][N].append(
                results_list[count + 3].get())
            results_dict['Heap Sort'][N].append(
                results_list[count + 4].get())
            count = count + 5

    draw_figure(results_dict)
    write_xlxs(results_dict)
