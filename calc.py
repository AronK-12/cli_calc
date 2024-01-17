import argparse

debug_equation:str = "1+2-3*4/20"
debug:bool = False

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

def solve_operation(num1:float, num2:float, op:str) -> float:
    match op:
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case _:
            return ValueError

def solve_MDAS(equation, operands):
    index:int = 0
    while operands[0] in equation or operands[1] in equation:
        number_1:float
        number_2:float
        operand:str

        if equation[index] == operands[0] or equation[index] == operands[1]:
            number_1 = float(equation[index - 1])
            number_2 = float(equation[index + 1])
            operand = equation[index]

            result:float = solve_operation(number_1, number_2, operand)

            equation.pop(index)
            equation.pop(index)
            equation[index - 1] = str(result)

            return equation
        index += 1

def solver(eq:list) -> list:
    new_list:list = eq

    while "*" in new_list or "/" in new_list:
        new_list = solve_MDAS(new_list, ["*", "/"])

    while "+" in new_list or "-" in new_list:
        new_list = solve_MDAS(new_list, ["+", "-"])

    return new_list

def main():
    if debug == False:
        parser = argparse.ArgumentParser(description='A Simple arithmetic calculator that can solve equations such as [1+2*5]')
        parser.add_argument('equation', 
                            help='''
                                can only contain integers and +-*/. No parenthesis.\n
                                If you want to use spaces between symbols and numbers, 
                                you have to wrap the argument between single or double quotes.''', 
                            type=str)
        args = parser.parse_args()

        splitted_equation = split_equation(args.equation)
    else:
        splitted_equation = split_equation(debug_equation)

    solved:float = float(solver(splitted_equation)[0])

    print(f'That equates to {round(solved, 2)}')

if __name__ == '__main__':
    main()