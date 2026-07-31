import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_tree(directory, prefix="    "):
    items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

    for item in items:
        if item.is_dir():
            print(prefix + Fore.BLUE + item.name + Style.RESET_ALL)
            print_tree(item, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + item.name + Style.RESET_ALL)


def main():
    if len(sys.argv) < 2:
        print("Треба вказати шлях до директорії, н.п:")
        print("python hw03.py /шлях/до/вашої/директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Шлях {path} не існує" + Style.RESET_ALL)
        return

    if not path.is_dir():
        print(Fore.RED + f"{path} не директорія" + Style.RESET_ALL)
        return

    print(Fore.BLUE + path.name + Style.RESET_ALL)
    print_tree(path)


if __name__ == "__main__":
    main()
