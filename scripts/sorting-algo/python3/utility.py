import os
import sys
import time
from random import randint


def cls(n=0):
    if n == 0:
        os.system('clear')
    else:
        print('\b'*n)


def parse_non_int(input_string: str) -> list:
    if input_string is None or input_string is "":
        return [0]
    new_string = ""
    accepted_string = [i for i in '1234567890 ']
    for i in input_string:
        if i in accepted_string:
            new_string += i
        elif i is ",":
            new_string += " "
        else:
            new_string += ""

    _ret = [int(i) for i in new_string.split(" ") if i is not '']
    return _ret


def visualizer(unsorted_list: list, pointer_position: int,
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
                         max_num=20, random_iteration=1000) -> list:
    if list_length == 0:
        list_length = 40
    if min_num == 0:
        min_num = 1
    if max_num == 0 or max_num <= min_num:
        max_num = min_num + 1
    if random_iteration == 0:
        random_iteration = 1

    ret_list: list = []
    random_number: int = 0

    for i in range(list_length):
        for _ in range(random_iteration):
            random_number = int(randint(min_num*100, max_num*100)/100)
        ret_list.append(random_number)

    return ret_list


def create_custom_list(input_string: str) -> list:
    return parse_non_int(input_string)
