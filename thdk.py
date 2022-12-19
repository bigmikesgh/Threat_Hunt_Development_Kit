from menus import *


def main():
    infile_opened = False

    while not infile_opened:
        infile_name = input("Enter analytic database file location: ")
        try:
            infile = open(infile_name, 'r')
            infile_opened = True
            infile.close()
        except FileNotFoundError:
            print("File not found. Please try again.\n")

    while True:
        main_menu_init()
        selection = input("\nEnter selection: ")

        if selection == '1':
            analytic_workspace_menu()

        elif selection == '2':
            display_by_mitre()

        elif selection == '0':
            break

        else:
            print("Something went wrong with your selection. Please try again.")


if __name__ == '__main__':
    main()
