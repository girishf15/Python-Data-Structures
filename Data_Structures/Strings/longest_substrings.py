

def largest_substring(expression):

    max_counter = 0
    temp_counter = 0

    if len(expression) == 0:
        return "Invalid Input"

    else:

        for i in range(1, len(expression)):

            if expression[i-1] == expression[i]:
                temp_counter += 1
            else:
                max_counter = max(max_counter, temp_counter)
                temp_counter = 1

        return max(max_counter, temp_counter)


s = "abcdddddeff"

print(largest_substring(s))
