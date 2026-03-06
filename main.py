import k_root as k
import calendar as cln
import cub_eq as eq


def main():
    """
    The main function.
    Gives the choice to user, what task to solve.
    """
    while True:
        print("--------------------------------------------------------------------")
        print("1. Calculating the number y =k√x")
        print("2. Calendar program")
        print("3. Solving a cubic equation x^3 + ax^2 + bx + c = 0")
        user_task = input("\nChoose a task to solve 1-3 (or any key to exit): ")

        match(user_task):
            case '1':
                k.get_number()
            case '2':
                cln.get_number()
            case '3':
                eq.get_number()
            case _:
                return

if __name__ == '__main__':
    main()