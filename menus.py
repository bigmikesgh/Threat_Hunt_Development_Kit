import os  # Importing operating system utilities
from colorama import Fore, Style  # Importing colorama
import analytic_builder


def main_menu_init():
    os.system('cls') # Clears Screen
    # Creates main menu
    print("Welcome to the TH-DK v0.01, the Threat Hunt Development Kit\n\n")
    print("""                                   _----..................___
     __,,..,-====>       _,.--''------'' |   _____  ______________`''--._
     \      `\   __..--''                |  /::: / /::::::::::::::\      \
      \       `''                        \r\t\t\t\t\t\t\t\t| /____/ /___ ____ _____::|    .  \r
       \         TH-DK    ,.... |            `    `     \_|   ( )  |
        `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
          `.                     |        ,'       `               `-.      |
            `-._                 \                                    ``.. /""")
    print(Fore.RED + "\t\t\t\t`---..............>")  # Adds a little blood to the blade
    print(Style.RESET_ALL) # Resets the color back to regular

    print("""1) Analytic Workspace
2) View analytics by MITRE mapping
3) Write analytics to a file
4) Build hunt plan
5) Record hunt
0) Exit TH-ADK""")


def analytic_workspace_menu():
    analytic = []
    while True:
        print("\n1) Build Analytic")
        print("2) Import Analytic")
        print("3) View Analytics")
        print("4) Edit Analytics")
        print("5) Save Analytic")
        print("9) Return to main menu")

        selection = input("\nEnter selection: ")

        if selection == '1':
            print("\nEntering build mode...\n")
            analytic.append(analytic_builder.build_analytic())
        elif selection == '2':
            print("Create import analytic function")
        elif selection == '3':
            print('Create function to retrieve analytics')
        elif selection == '4':
            print('Create function to edit analytics')
        elif selection == '9':
            break
        else:
            print('Invalid selection please try again')


def display_by_mitre():
    print("Persistence -78 | Credential Access - 34 | Command & Control")
    print("\nEnter Analytic ID: ")
