opertors = ['+', '-', '*', '/']


def postfix(expression):

    if len(expression) == 0:
        print("invalid expression")
        return

    stack = []

    for val in expression:

        if val not in opertors:
            stack.append(val)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(str(eval(val2 + val + val1)))

    print("Final result : {}".format(stack[0]))


exp = "231*+9-"
postfix(exp)

postfix("")
