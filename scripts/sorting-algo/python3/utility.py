import os
import sys
import time
from random import randint


def cls(n=0):
    if n == 0:
        os.system('clear')
    else:
        print('\b'*n)


def visualizer(unsorted_list, pointer_position,
               more_val="", wait=0.04, original_list=None) -> str:
    cls()
    s = ""
    if(original_list is not None):
        s += str(original_list) + "\n"

    s += str(unsorted_list) + "\n"
    for i in range(len(unsorted_list)):
        s += "#" * unsorted_list[i]

        s += " " * int((max(unsorted_list) - unsorted_list[i]) + 2)

        s += (str(unsorted_list[i]))
        if(i == pointer_position):
            s += "  <-- [" + str(pointer_position) + "]" + \
                " " + str(more_val) + "\n"
        else:
            s += "\n"

    # s += "\n\n"
    cls()
    print(s)
    sys.stdout.flush()
    time.sleep(wait/1.5)


def generate_random_list(list_length=40, min_num=1,
                         max_num=100, random_iteration=1000) -> list:
    ret_list = []
    random_number = 0

    for i in range(list_length):
        for _ in range(random_iteration):
            random_number = int(randint(min_num*100, max_num*100)/100)
        ret_list.append(random_number)

    return ret_list
