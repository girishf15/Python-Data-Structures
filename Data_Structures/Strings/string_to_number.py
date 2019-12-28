__author__ = "Girish Fedram"

#additional dependencies
import re

def number_string_mapping(number):
    """
    This function performs the mapping of the string number/
    to the string digit and returns it

    Arguments:
        number string -- string number value in lower case

    Returns:
        string -- returns digit in string format
    """

    #dictionary of string to number mapping
    units = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
             "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    #extract all the keys
    number_keys = units.keys()

    #if key exists return number else return None
    if number in number_keys:
        return units[number]

    return None


def stringToNumber(camelCaseString):
    """
    This function takes the camelcase string, splits it and calls \
    numberstringmapping to generate number

    Arguments:
        camelCaseString string -- camelcase string for conversion
    """

    #extract all the string numbers using regular expression
    string_number_list = re.findall("[a-zA-Z][^A-Z]*", camelCaseString)

    #call the string_to_number mapping function
    number_list = [number_string_mapping(x.lower()) for x in string_number_list]

    #converts the number list into the number
    final_number = int("".join(filter(lambda x: x, number_list)))

    print(final_number)


#STRING = input('Enter Digits in CamelCase: ')
STRING = "oneTwoFourThreeTwoFiveSevenNine"
stringToNumber(STRING)

#if valid string number is not entered it will skip that number
#eg: onetwoThree ----> output will be 3
