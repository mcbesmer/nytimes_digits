def find_expression(numbers, target, expression="", num_ops=0, best_solution=None):
    """
    Recursively generate all possible expressions using the given numbers
    and evaluate them to see if they are equal to the target value.
    """
    if target in numbers:
        # base case: if the list contains the target, return it
        expression += str(numbers[0])
        result = numbers[0]
        if abs(result - target) < 0.0001:
            print(expression + " = " + str(result))
            if best_solution is None or num_ops < best_solution[1]:
                return (expression, num_ops)
            else:
                return best_solution
        else:
            return best_solution

    if best_solution is not None and num_ops >= best_solution[1]:
        return best_solution

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # select the i-th and j-th numbers as the operands
            first, second = numbers[i], numbers[j]
            # create a new list of numbers with the i-th and j-th elements removed
            remaining = [num for idx, num in enumerate(numbers) if idx not in [i, j]]

            # check if any operand or intermediate result is negative
            if first < 0 or second < 0:
                continue

            # recursively generate expressions using the remaining numbers
            for operator in ["+", "-", "*", "/"]:
                # try all four basic arithmetic operations
                if operator == "+":
                    sub_expression = expression + str(first) + " + " + str(second) + " "
                    sub_result = find_expression([first + second] + remaining, target, sub_expression, num_ops+1, best_solution)
                    if sub_result is not None:
                        if best_solution is None or sub_result[1] < best_solution[1]:
                            best_solution = sub_result
                elif operator == "-":
                    if first < second:
                        continue
                    sub_expression = expression + str(first) + " - " + str(second) + " "
                    sub_result = find_expression([first - second] + remaining, target, sub_expression, num_ops+1, best_solution)
                    if sub_result is not None:
                        if best_solution is None or sub_result[1] < best_solution[1]:
                            best_solution = sub_result
                elif operator == "*":
                    sub_expression = expression + str(first) + " * " + str(second) + " "
                    sub_result = find_expression([first * second] + remaining, target, sub_expression, num_ops+1, best_solution)
                    if sub_result is not None:
                        if best_solution is None or sub_result[1] < best_solution[1]:
                            best_solution = sub_result
                elif operator == "/":
                    if second == 0:
                        continue
                    if first % second != 0:
                        continue
                    sub_expression = expression + str(first) + " / " + str(second) + " "
                    sub_result = find_expression([first / second] + remaining, target, sub_expression, num_ops+1, best_solution)
                    if sub_result is not None:
                        if best_solution is None or sub_result[1] < best_solution[1]:
                            best_solution = sub_result

    # if we've exhausted all possibilities and haven't found a match, return None
    return best_solution



numbers = [2, 3, 4, 5, 10, 25]
target = 56

result = find_expression(numbers, target)
print(f"An expression that evaluates to {target} is: {result}")
