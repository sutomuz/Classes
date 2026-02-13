from menu import Menu

def main():
    menu = Menu()
    menu.addOption("Check available memory")
    menu.addOption("View network connections")
    menu.addOption("Display free ram and swap")
    menu.addOption("Quit")

    menu.run()

if __name__ == "__main__":
    main()
