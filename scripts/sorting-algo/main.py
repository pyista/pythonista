from __future__ import print_function
from utility import *

def selection_sort(input_list:list) -> list:
    original_list = sorted(input_list)
    unsorted_list = input_list.copy()
    carried_value:int
    cv_position:int
    pointer_value:int = 0

    pointer_position:int = 0
    sorted_position:int = 0

    lowest_value:int = 0
    lv_position:int

    is_sorted:bool = False
    while not is_sorted:
        carried_value = unsorted_list[sorted_position]
        for i in range(len(unsorted_list) - sorted_position):
            pointer_position = i + sorted_position
            pointer_value = unsorted_list[pointer_position]
            if pointer_value <= carried_value:
                carried_value = pointer_value
                cv_position = pointer_position
            visualizer(unsorted_list, pointer_position, carried_value, original_list=original_list)

        # -- Swap --
        unsorted_list[cv_position] = unsorted_list[sorted_position]
        unsorted_list[sorted_position] = carried_value
        visualizer(unsorted_list, pointer_position, wait=False, original_list=original_list)

        pointer_value = 0
        pointer_position = 0
        lowest_value = 0
        lv_position = 0
        carried_value = 0
        sorted_position += 1

        if(sorted_position >= len(unsorted_list)):
            break
