import sys
import colorama
from random import randint
from time import sleep
colorama.init()
sys.argv.pop(0)


def help():
    print(
        f"""
{colorama.Fore.MAGENTA}Dice roller:{colorama.Fore.RESET}
{colorama.Fore.LIGHTYELLOW_EX}Simple dice roller.{colorama.Fore.RESET}

Usage:
    {colorama.Fore.GREEN}# cd to the directory of the script{colorama.Fore.RESET}
    {colorama.Fore.YELLOW}python3 dice_roll.py [amount of dices (default: 1)] [amount of sides (default: 6)]{colorama.Fore.RESET}
"""
    )

# very stupid way of giving the user a help list, but it works
# I'm not sure how to do it better
#  create an issue on github if you know how to do it better
def main():
    try:
        # ! doesn't work
        # todo: fix this
        #    if sys.argv[] == "help":
        #        help()
        # check if arguments exist, otherwise set default values
        if len(sys.argv) == 0:
            amount_of_dices = 1
            amount_of_sides = 6
            print(f"{colorama.Fore.LIGHTBLACK_EX}Setting 2 default values: {colorama.Fore.LIGHTBLUE_EX}{amount_of_dices}:{amount_of_sides}{colorama.Fore.RESET}")
        elif len(sys.argv) > 1:
            amount_of_dices = int(sys.argv[0])
            amount_of_sides = int(sys.argv[1])
        elif len(sys.argv) == 1:
            amount_of_dices = int(sys.argv[0])
            amount_of_sides = 6
            print(f"{colorama.Fore.LIGHTBLACK_EX}Setting 1 default value: {colorama.Fore.LIGHTBLUE_EX}{amount_of_dices}:{amount_of_sides}{colorama.Fore.RESET}")
        else:
            return print(f"{colorama.Fore.RED}Error: Too many arguments provided.{colorama.Fore.RESET}")

        # roll the dice
        print(f"{colorama.Fore.GREEN}Rolling {colorama.Fore.LIGHTBLUE_EX}{amount_of_dices}:{amount_of_sides}{colorama.Fore.RESET}...")
        sleep(float(3))

        # print results based on amount of dices
        if amount_of_dices == 1:
            result = randint(1, amount_of_sides)
            print(
                f"{colorama.Fore.GREEN}Result: {colorama.Fore.LIGHTBLUE_EX}{result}{colorama.Fore.RESET}")
        else:
            for i in range(amount_of_dices):
                result = randint(1, amount_of_sides)
                print(
                    f"{colorama.Fore.GREEN}Result {i + 1}: {colorama.Fore.LIGHTBLUE_EX}{result}{colorama.Fore.RESET}")
    except:
        return help()


if __name__ == '__main__':
    main()
