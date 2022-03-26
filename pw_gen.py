import sys
import colorama
import random
import pyperclip
sys.argv.pop(0)
colorama.init()


def help():
    print(
        f"""
{colorama.Fore.MAGENTA}Password Generator:{colorama.Fore.RESET}
{colorama.Fore.LIGHTYELLOW_EX}A password generator that will (obviously) generate a password for you.
With this, you can save passwords into a file and copy them too.{colorama.Fore.RESET}

Usage:
    {colorama.Fore.GREEN}# cd to the directory of the script{colorama.Fore.RESET}
    {colorama.Fore.YELLOW}python3 pw_gen.py [length of passwords (default: 8)]{colorama.Fore.RESET}
""")  # noqa


def main():
    password = ""
    length = 8

    if len(sys.argv) > 0:
        if sys.argv[0] == "help":
            help()
        elif sys.argv[0].isdigit():
            length = int(sys.argv[0])
        else:
            return print(f"{colorama.Fore.RED}Error: Invalid length.{colorama.Fore.RESET}")  # noqa

    for char in range(int(length)):
        password += random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")  # noqa

    print(f"{colorama.Fore.GREEN}Password: {colorama.Fore.LIGHTBLUE_EX}{password}{colorama.Fore.RESET}")  # noqa

    if not pyperclip.copy:
        print(f"{colorama.Fore.RED}Error: Could not copy to clipboard.{colorama.Fore.RESET}")  # noqa
    else:
        pyperclip.copy(password)
        print(f"{colorama.Fore.MAGENTA}Password copied to clipboard.{colorama.Fore.RESET}")  # noqa

    usr = input("Would you like to save this password to a file? (y/n): ")
    if usr == "y":
        pw_dir = input(
            "Where would you like to save the password? (default: ./pw.txt): ")

        if pw_dir == "":
            pw_dir = "./pw.txt"
        try:
            with open(pw_dir, "w") as pw_file:
                pw_file.write(password)
                print(f"{colorama.Fore.GREEN}Password saved to {pw_dir}{colorama.Fore.RESET}")  # noqa
        except PermissionError:
            print(f"{colorama.Fore.RED}Error: Could not save password to \"{pw_dir}\". Not enough permissions{colorama.Fore.RESET}")  # noqa


if __name__ == '__main__':
    main()
