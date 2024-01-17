import argparse

def split_equation(eq:str) -> list:
    """
    Splits a mathematical equation represented as a string into a list of operands and operators.

    Parameters:
    - eq (str): The input mathematical equation as a string.

    Returns:
    - list: A list containing operands and operators from the input equation.

    Example:
    >>> split_equation("3 + 5 * 20-3")
    ['3', '+', '5', '*', '20']
    """
    eq_list:list = []

    current = ""

    for item in eq:
        if item == "+" or item == "-" or item == "*" or item == "/":
            eq_list.append(current)
            eq_list.append(item)
            current = ""
        else:
            current += item

    eq_list.append(current)


    return eq_list

def main():
    parser = argparse.ArgumentParser(description='A Simple arithmetic calculator that can solve equations such as [1+2*5]')
    parser.add_argument('equation', help='can only contain integers and +-*/. No parenthesis.', type=str)

    args = parser.parse_args()

    splitted_equation = split_equation(args.equation)


if __name__ == '__main__':
    main()