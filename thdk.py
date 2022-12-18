from menus import *


def main():
    selection = ''
    while True:
        main_menu_init()
        selection = input("\nEnter selection: ")

        if selection == '1':
            analytic_builder_menu()

        elif selection == '2':
            display_by_mitre()

        elif selection == '0':
            break

        else:
            print("Something went wrong with your selection. Please try again.")


if __name__ == '__main__':
    main()
