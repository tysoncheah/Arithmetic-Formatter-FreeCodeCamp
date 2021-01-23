def check_arranger(number1, operator, number2):
    try:
        if operator != '+' and operator != '-':
            raise Exception
    except:
        return "Error: Operator must be '+' or '-'."
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise Exception
    except:
        return "Error: Numbers cannot be more than four digits."
    return ""


def arithmetic_arranger(problems, displayMode=False):
    try:
        if len(problems) > 5:
            raise Exception
    except:
        return "Error: Too many problems."

    first = True
    four_space = '    '
    line1 = line2 = line3 = line4 = ""

    for problem in problems:
        separated_problem = problem.split()
        number1 = separated_problem[0]
        operator = separated_problem[1]
        number2 = separated_problem[2]
        check = check_arranger(number1, operator, number2)
        if check != "":
            return check
        maxspace = max(len(number1), len(number2))
        no1 = int(number1)
        no2 = int(number2)
        if first == True:
            line1 += number1.rjust(maxspace + 2)
            line2 += operator + ' ' + number2.rjust(maxspace)
            line3 += '-' * (maxspace + 2)
            if displayMode == True:
                if operator == "+":
                    line4 += str(no1 + no2).rjust(maxspace + 2)
                else:
                    line4 += str(no1 - no2).rjust(maxspace + 2)
            first = False

        else:
            line1 += four_space + number1.rjust(maxspace + 2)
            line2 += operator.rjust(5) + " " + number2.rjust(maxspace)
            line3 += four_space + "-" * (maxspace + 2)
            if displayMode == True:
                if operator == "+":
                    line4 += four_space + str(no1 + no2).rjust(maxspace + 2)
                else:
                    line4 += four_space + str(no1 - no2).rjust(maxspace + 2)

    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
