from run_bash_cmd_function import run_bash_cmd

class Menu:
    # Constructs a menu with no options
    def __init__(self):
        self._options = []

    # Adds an option to the end of this menu
    def addOption(self, option):
        self._options.append(option)

    # Displays the menu and returns valid user input
    def getInput(self):
        while True:
            print()
            for i, opt in enumerate(self._options, start=1):
                print(f"{i} {opt}")

            user_choice = input("Your Input: ").strip()

            try:
                user_choice = int(user_choice)
            except ValueError:
                print("Invalid option. Try again.\n")
                continue

            if 1 <= user_choice <= len(self._options):
                return user_choice

            print("Invalid option. Try again.\n")

    # Runs the menu until user selects Quit
    def run(self):
        while True:
            choice = self.getInput()

            if choice == 4:
                break

            run_bash_cmd(choice)
