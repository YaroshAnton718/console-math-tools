import numpy as np

def get_number():
    """
    Gets from user the coefficients of cubic equation.
    Validates the user input.
    Prints result to console.
    """
    print("\n----------Cubic equation----------")

    while True:
        while True:
            try:
                coef_a = float(input("Enter coefficient a [-9999; 9999]: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if coef_a < -9999 or coef_a > 9999:
                print("Please enter a number between [-9999; 9999].")
                continue
            else:
                break

        while True:
            try:
                coef_b = float(input("Enter coefficient b [-9999; 9999]: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if coef_b < -9999 or coef_b > 9999:
                print("Please enter a number between [-9999; 9999].")
                continue
            else:
                break

        while True:
            try:
                coef_c = float(input("Enter coefficient c [-9999; 9999]: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if coef_c < -9999 or coef_c > 9999:
                print("Please enter a number between [-9999; 9999].")
                continue
            else:
                break

        break

    result = cubic_equation(coef_a, coef_b, coef_c)
    for i in range(len(result)):
        print(f"x[{i}] = {result[i]}")

    print("")

def cubic_equation(a, b, c):
    """
    Calculates the cubic equation with coefficients a, b, and c.
    Uses the library NumPy for solving.

    Parameters:
        a (float): coefficient 'a' of cubic equation.
        b (float): coefficient 'b' of cubic equation.
        c (float): coefficient 'c' of cubic equation.

    Returns:
        roots (list): The list of roots of the equation.
    """
    coeffs = [1, a, b, c]
    roots = np.roots(coeffs)

    return roots
