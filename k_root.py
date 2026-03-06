import gmpy2

def get_number():
    """
    Gets from user the arguments of root.
    Validates the user input.
    Prints result to console.
    """
    print("\n----------Root calculator----------")

    while True:
        while True:
            try:
                k = int(input("Enter k (-99; 99): "))
            except ValueError:
                print("Please enter a number.")
                continue

            if k <= -100 or k >= 100:
                print("Please enter a number between -99 and 99.")
                continue
            else:
                break

        while True:
            try:
                x = float(input("Enter x (-9999; 9999): "))
            except ValueError:
                print("Please enter a number.")
                continue

            if x <= -10000 or x >= 10000:
                print("Please enter a number between -9999 and 9999.")
                continue
            else:
                break

        while True:
            try:
                eps = int(input("Enter precision [1; 10]: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if eps < 1 or eps > 10:
                print("Please enter a number between 1 and 10.")
                continue
            else:
                break

        if k % 2 == 0 and x < 0:
            print("There is no solution. When k is even, then x cannot be less than 0.")
            continue
        else:
            break

    print(f"Result: {root_calculation(k, x, eps)}\n")

def root_calculation(k, x, eps):
    """
    Calculates the root of the number.

    Parameters:
        k (int): k-root
        x (float): the number to calculate the root of
        eps (int): precision of result

    Returns:
        result (float) : root of the number
    """
    res = float(gmpy2.root(x, k))
    result = round(res, eps)

    return result