import os

LINE = "-" * 80

# Keep commands in one place (easier to maintain)
COMMANDS = {
    1: ("The available memory is", "free -tmh"),
    2: ("The current network connections include",
        "netstat -an | grep -i Estab | awk '{print $5}' | cut -d: -f1 | sort | uniq -c"),
    3: ("Available file space is",
        r'df -h | grep -E "Filesystem|/root"'),
}

def run_bash_cmd(some_choice: int) -> None:
    """
    Runs a Linux utility based on the menu choice (1-3).
    Prints a header line and the user's choice like the professor example.
    """
    print(f"{LINE}\n")
    print("You entered #", some_choice)

    info = COMMANDS.get(some_choice)
    if not info:
        print("Invalid option.")
        return

    label, cmd = info
    print(label + ":")
    os.system(cmd)
