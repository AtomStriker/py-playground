import sys
import colorama
colorama.init()
sys.argv.pop(0)


def help():
    print(
        f"""
{colorama.Fore.MAGENTA}Email Slicer:{colorama.Fore.RESET}
{colorama.Fore.LIGHTYELLOW_EX}This is a simple email slicer, giving you the name, domain, and extension of an email address.{colorama.Fore.RESET}
{colorama.Fore.LIGHTBLACK_EX}NOTE: This doesn't check for email address validations (yet), neither does it check the safety of a domain.{colorama.Fore.RESET}

Usage:
    {colorama.Fore.GREEN}# cd to the directory of the script{colorama.Fore.RESET}
    {colorama.Fore.YELLOW}python3 email_slicer.py [email]{colorama.Fore.RESET}
"""
    )
    sys.exit()


def main():
    # check if arguments exist
    if len(sys.argv) == 0:
        return print(f"{colorama.Fore.RED}Error: No arguments provided.{colorama.Fore.RESET}")

    # call help function if help is passed as an argument
    if sys.argv[0] == "help":
        help()

    # check if email has a valid format
    if "@" not in sys.argv[0]:
        return print(f"{colorama.Fore.RED}Error: Invalid email format.{colorama.Fore.RESET}")
    else:
        print(
            f"{colorama.Fore.GREEN}Full Email: {colorama.Fore.LIGHTBLUE_EX}{sys.argv[0]}{colorama.Fore.RESET}")

    email = sys.argv[0].split("@")[0]
    print(
        f"{colorama.Fore.GREEN}User: {colorama.Fore.LIGHTBLUE_EX}{email}{colorama.Fore.RESET}")

    domain = sys.argv[0].split("@")[1]
    if "." not in domain:
        return print(f"{colorama.Fore.RED}Error: Domain is not valid.{colorama.Fore.RESET}")
    else:
        print(
            f"{colorama.Fore.GREEN}Domain: {colorama.Fore.LIGHTBLUE_EX}{domain}{colorama.Fore.RESET}")


if __name__ == '__main__':
    main()
