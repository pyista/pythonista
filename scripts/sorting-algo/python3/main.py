from sortalgo import selection_sort
from utility import generate_random_list
from interface import *


class Main:
    def __init__(self):
        self.my_list: list = None
        self.first_opened: bool = True

    def run(self) -> None:
        while True:
            mm: int = main_menu(self.first_opened, self.my_list)
            self.first_opened = False
            if mm == 0:
                return
            elif mm == 1:
                self.create_list(create_list_submenu())
                continue
            elif mm == 2:
                if self.my_list is None:
                    system('clear')
                    print("You are not yet configure your list !")
                    print("Please refer to menu 1 !")
                    print()
                    input("Press Enter to Continue")
                    continue
                else:
                    self.do_sort()
                    input("Press Enter to Continue")
                    continue
            elif mm == 3:
                tutorial(True)
                input("\n\nPress Enter to Continue")
                continue
            else:
                continue

    def create_list(self, choice: int):
        while True:
            if choice == 0:
                return
            elif choice == 1:
                self.my_list = ask_custom_list()
                return
            elif choice == 2:
                self.my_list = ask_random_list()
                return
            else:
                continue

    def do_sort(self):
        try:
            selection_sort(self.my_list)
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    my_app: Main = Main()
    while True:
        try:
            my_app.run()
        except KeyboardInterrupt:
            pass
