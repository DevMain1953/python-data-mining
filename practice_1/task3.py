def get_operation_result(first_operand, second_operand, operation) -> float:
    if operation == "+":
        return first_operand + second_operand
    if operation == "-":
        return first_operand - second_operand
    if operation == "/":
        try:
            return first_operand / second_operand
        except ZeroDivisionError:
            return 0.0
    if operation == "//":
        try:
            return first_operand // second_operand
        except ZeroDivisionError:
            return 0.0
    if operation == "**":
        return first_operand ** second_operand


if __name__ == '__main__':
    print(get_operation_result(int(input("Enter first operand ")), int(input("Enter second operand ")),
                               str(input("Enter operation "))))
