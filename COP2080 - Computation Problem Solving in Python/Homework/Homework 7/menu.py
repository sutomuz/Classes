from run_bash_cmd_function import run_bash_cmd

class Menu:
    # constructs frame of menu
    def __init__(self):
        self._options = []

    # adds an option to the end
    def addOption(self, option):
        self._options.append(option)

    # displays the menu and returns users input
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

    # runs the menu until user quits
    def run(self):
        while True:
            choice = self.getInput()

            if choice == 4:
                break

            run_bash_cmd(choice)
