open_list = ['(', '{', '[']
close_list = [')', '}', ']']


def check_para(my_str):

    stack = []

    for ch in my_str:

        if ch in open_list:
            stack.append(ch)

        elif ch in close_list:
            pos = close_list.index(ch)

            if (len(stack) > 0) and open_list[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                print("Unbalanced...!!")
                break

    if len(stack) == 0:
        print("Balanced...!!")


# Driver code
string = "{[]{()}}"
check_para(string)

string = "[{}{})(]"
check_para(string)
