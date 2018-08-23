from utility import visualizer


def selection_sort(input_list: list) -> list:
    unsorted_list = input_list.copy()
    carried_value = 0
    cv_position = 0
    pointer_value = 0

    pointer_position = 0
    sorted_position = 0

    while sorted_position != len(unsorted_list):
        carried_value = unsorted_list[sorted_position]
        for i in range(len(unsorted_list) - sorted_position):
            pointer_position = i + sorted_position
            pointer_value = unsorted_list[pointer_position]
            if pointer_value <= carried_value:
                carried_value = pointer_value
                cv_position = pointer_position
            visualizer(unsorted_list, pointer_position, carried_value)

        # -- Swap --
        unsorted_list[cv_position] = unsorted_list[sorted_position]
        unsorted_list[sorted_position] = carried_value
        visualizer(unsorted_list, pointer_position, wait=0)

        pointer_value = 0
        pointer_position = 0
        carried_value = 0
        sorted_position += 1

    return unsorted_list
