import os, sys, time
from random import randint

def visualizer(unsorted_list:list, pointer_position:int, more_val="", wait=0.032, original_list:list=None) -> None:
    os.system('clear')
    sys.stdout.flush()
    s = ""
    if(original_list is not None):
        s += str(original_list) + "\n"

    s += str(unsorted_list) + "\n"
    for i in range(len(unsorted_list)):
        s += "#" * unsorted_list[i]

        s += " " * int((max(unsorted_list) - unsorted_list[i]) + 2)

        s+=(str(unsorted_list[i]))
        if(i == pointer_position):
            s += "  <-- [" + str(pointer_position) + "]" + " " + str(more_val) + "\n"
        else:
            s += "\n"

    sys.stdout.flush()
    sys.stdout.writelines(s)
    time.sleep(wait)
    os.system('clear')

def generate_random_list(list_length:int=40, min_num:int=1, max_num:int=10, random_iteration:int=1000) -> list:
    ret_list:list = []
    random_number:int

    for i in range(list_length):
        for _ in range(random_iteration):
            random_number = randint(min_num, max_num)
        ret_list.append(random_number)

    return ret_list