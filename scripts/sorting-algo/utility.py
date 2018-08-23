import os, sys
def visualizer(unsorted_list:list, pointer_position:int, more_val="", wait=True, original_list:list=None) -> None:
    os.system('clear')
    if(original_list is not None):
        print(original_list)
    print(unsorted_list)
    for i in range(len(unsorted_list)):
        for j in range(unsorted_list[i]):
            print("-", end="")

        for k in range((max(unsorted_list)-unsorted_list[i])+2):
            print(" ", end="")

        print(unsorted_list[i], end="")
        if(i == pointer_position):
            print("  <-- [" + str(pointer_position) + "]" + " " + str(more_val))
        else:
            print()
        sys.stdout.flush()
    if(wait):
        time.sleep(0.05)

